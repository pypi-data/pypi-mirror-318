# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import datetime
import glob
import hashlib
import os
import pathlib
import re
import squish
import tempfile
import test
from remotesystem import RemoteSystem
from typing import Tuple

import mrcfile
from lxml import etree
from PIL import Image, UnidentifiedImageError
from utils.string_utils import remove_chars
from velox.labels.time_constants import TimeOut

from .execution_info import log_attached_file
from .process import Process
from .wildcard import WildCard


def find_svg_image_size(file_name: str) -> tuple:
    try:
        document = etree.parse(file_name)
    except etree.ParseError as e:
        test.fail("Cannot process file %s: Reason: %s" % (file_name, e))

    if document is None:
        test.fail("Content of file %s is invalid." % file_name)

    svg = document.getroot()

    image_element = svg.find("./{*}g/{*}image")
    width = int(image_element.get("width"))
    height = int(image_element.get("height"))

    return (width, height)


class FileUtils:
    def __init__(self, connection=RemoteSystem()):
        self.connection = connection

    def directory_exists(self, directory: str) -> bool:
        """Checks if the directory exist and is of the type directory.

        Parameters
        ----------
        directory: Full directory path

        Returns
        -------
        True if the directory exists otherwise False
        """

        return self.connection.exists(directory) and self.connection.stat(directory, "isDir")

    def file_exists(self, filepath: str) -> bool:
        """Checks if the file exist and is of the type file.

        Parameters
        ----------
        filepath: Full file path

        Returns
        -------
        True if the file exists otherwise False
        """
        filepath = remote_path(filepath)
        try:
            return self.connection.exists(filepath) and self.connection.stat(filepath, "isFile")
        except Exception as ex:
            test.warning(f"{repr(ex)}")
            return False

    def file_is_not_locked(self, filepath: str) -> bool:
        """Ensure file is not use by another process."""
        try:
            new_name = f"{filepath}copy"
            self.connection.rename(filepath, new_name)
            self.connection.rename(new_name, filepath)
            return True
        except Exception:
            return False

    def create_directory(self, directory: str):
        """Creates the directory if it does not exist yet.

        Parameters
        ----------
        directory: Directory to create
        """
        if not self.directory_exists(directory):
            test.log(f"Creating new folder: {directory}")
            self.connection.createPath(directory)
        assert self.directory_exists(directory), f"Unable to create directory {directory}"

    def delete_directory(self, path: str, recursive=False):
        """Deletes a given directory from the remote system (where Squish server is running).

        Parameters
        ----------
        path: the path to the directory to be deleted
        recursive: whether the deletion should be recursive or not

        Raises
        ------
        OSError when directory exists but cannot be deleted after timeout is reached.
        """
        if not self.directory_exists(path):
            test.log(f"Cannot delete directory at path '{path}'. No directory exists at that path.")
            return

        def successfully_deleted_directory() -> bool:
            """Tries to delete the directory and returns True if successful.

            If the directory cannot be deleted, as is the case when a file is locked or permissions are not correct,
            this function returns False.
            """
            try:
                self.connection.deleteDirectory(path, recursive)
                return not self.directory_exists(path)
            except Exception:
                return False

        if not squish.waitFor(successfully_deleted_directory, TimeOut.DIRECTORY_DELETION.milliseconds):
            raise OSError(f"Could not delete directory at path '{path}'")

    def empty_directory(self, path: str):
        self.delete_directory(path, recursive=True)
        self.create_directory(path)

    def update_file_creation_to_now(self, filename: str) -> bool:
        """Brief update the creation/last modification time of the given file with the current time using powershell.

        Parameters
        ----------
        filename: Name of filename to set creation/write time stamp to now

        Returns
        -------
        True if update succeeded
        """
        now = datetime.datetime.now()
        args = ["powershell", "Get-ChildItem", "'{}'".format(filename), "|", "% {{$_.CreationTime = '{}'}}".format(now)]
        (exitcode_creation_time, stdout, stderr) = self.connection.execute(args)
        args = [
            "powershell",
            "Get-ChildItem",
            "'{}'".format(filename),
            "|",
            "% {{$_.LastWriteTime = '{}'}}".format(now),
        ]
        (exitcode_write_time, stdout, stderr) = self.connection.execute(args)
        return int(exitcode_creation_time) == 0 and int(exitcode_write_time) == 0

    def delete_file(self, file: str):
        """Delete file at given location.

        Parameters
        ----------
        file: Full path to file to delete
        """
        # this validation is needed to avoid problems
        # if a command is passed as the file path to the `execute` method below
        if not self.file_exists(file):
            raise FileNotFoundError(f"The file '{file}' doesn't exist.")

        # `RemoteSystem.execute` is used instead of `RemoteSystem.deleteFile`
        # because the latter doesn't have access to the file
        # when that file is an experiment that was open when Velox was killed
        exitcode, stdout, stderr = self.connection.execute(["cmd", "/c", "del", "/F", file])

        if self.file_exists(file):
            raise RuntimeError(
                f"It was not possible to delete the file {file}. "
                f"exitcode: {exitcode} ;"
                f"stdout: {stdout} ;"
                f"stderr: {stderr}"
            )

    def delete_read_only_file(self, file: str):
        """Delete a read only file at given location.

        Parameters
        ----------
        file: Full path to file to delete
        """
        self.remove_readonly_attrib(file)
        self.connection.deleteFile(file)

    @staticmethod
    def remove_readonly_attrib(file: str):
        """Removes the read-only attrib from a file using the attrib command.

        Parameters
        ----------
        file: File to remove the readonly attribute from
        """
        (exitcode, stdout, stderr) = Process().start(["attrib", "-r", file])
        assert (
            exitcode == "0"
        ), f"Unable to remove readonly attribute of file {file}, stdout: {stdout}, stderr: {stderr}"

    def copy_file(self, source_file: str, destination_file: str, overwrite_destination: bool = True):
        """Copy file from given source to destination.

        Parameters
        ----------
        source_file: Full path to source file
        destination_file: Full path to destination file
        overwrite_destination: Overwrite destination file
        """
        if overwrite_destination and self.file_exists(destination_file):
            self.delete_file(destination_file)
        assert self.connection.copy(
            source_file, destination_file
        ), f"Unable to copy {source_file} to {destination_file}"
        assert self.file_exists(
            destination_file
        ), f"File {destination_file} was not found after copy from {source_file}"

    def copy_directory(self, source_path: str, destination_path: str):
        assert self.connection.copy(
            source_path, destination_path
        ), f"Unable to copy {source_path} to {destination_path}"

    def get_creation_date(self, filename: str) -> datetime:
        """Gets the creation date of a file as a Timestamp.

        Parameters
        -----------
        filename: Full path to file

        Returns
        -------
        The creation date as a Timestamp
        """
        return self.connection.stat(filename, "lastRead")

    def get_modification_date(self, filename: str) -> datetime:
        """Gets the modification date of a file as a Timestamp.

        Parameters
        -----------
        filename: Full path to file

        Returns
        -------
        The modification date as a Timestamp
        """
        return self.connection.stat(filename, "lastModified")

    def file_version(self, filename: str) -> str:
        """Returns the file version of the given file.

        Parameters
        ----------
        filename: full name of the file to get the version from

        Returns
        -------
        File version. String "Unknown" when no version was found
        """

        call_filename = "name='{}'".format(filename.replace("\\", "\\\\"))
        version_search = "Version="
        args = ["wmic", "datafile", "where", call_filename, "get", r"Version", "/value"]
        (exitcode, stdout, stderr) = self.connection.execute(args)
        if int(exitcode) != 0:
            return "Unknown"
        if stdout.find(version_search) != -1:
            return (stdout[stdout.find(version_search) + len(version_search) :]).strip()
        return "Unknown"

    @classmethod
    def convert_wild_card_to_regex(cls, wild_card: str) -> str:
        """Returns the regular expression version of a wildcard.

        Parameters
        ----------
        wild_card: Wildcard to convert

        Returns
        -------
        Wild card as a regex string
        """

        wild_card = wild_card.replace(".", r"\.").replace("?", ".").replace("*", ".*")
        # add line end and start
        return "^" + wild_card + "$"

    @staticmethod
    def get_remote_temp_dir() -> str:
        """Returns the remote temp directory.

        Returns
        -------
        Remote temp directory as a string.
        """
        return RemoteSystem().getEnvironmentVariable("TEMP")

    def get_directories(self, directory, wild_card: str = "*", recursive: bool = False) -> list:
        """Returns a list of directories.

        Parameters
        ----------
        directory: Directory to get the list of directories from
        wild_card: Wildcard to select a specific set of files
        recursive: States if the function should also check sub-directories of the given directory

        Returns
        -------
        List of directories as a string array
        """

        directory_content = self.get_directory_content(directory, wild_card, recursive)
        return [file_path for file_path in directory_content if self.connection.stat(os.path.join(file_path), "isDir")]

    def get_directory_content(self, directory: str, wild_card: str = "*.*", recursive: bool = False) -> list:
        """Return a list of files/directories of full file names located in the given directory. Directories defined as
        a symbolic link will not be followed due to limitations of the RemoteSystem object of Squish (Files within
        symbolic link directory are not found)

        Parameters
        ----------
        directory: Directory to get the list of files/directories from
        wild_card: Wildcard to select a specific set of files
        recursive: States if the function should also check sub-directories of the given directory

        Returns
        -------
        List of files/directories as a string array
        """
        directory = remote_path(directory)

        if not self.directory_exists(directory):
            return []

        wild_card = WildCard(wild_card)

        def _recurse(parent_path, recurse_wild_card: WildCard):
            result = []
            files = self.connection.listFiles(parent_path)
            for filepath in files:
                filepath = os.path.join(parent_path, filepath)

                if self.connection.stat(filepath, "isDir"):
                    # we ignore symlinks because we can not iterate its content
                    if self.connection.stat(filepath, "isSymLink"):
                        continue
                    if recurse_wild_card.search(filepath):
                        result.append(filepath)
                    result.extend(_recurse(filepath, wild_card))
                elif recurse_wild_card.search(filepath):
                    result.append(filepath)

            return result

        def _list(parent_path, list_wild_card: WildCard):
            result = []
            files = self.connection.listFiles(parent_path)
            for filepath in files:
                filepath = os.path.join(parent_path, filepath)

                if list_wild_card.search(filepath):
                    result.append(filepath)

            return result

        if recursive:
            return _recurse(directory, wild_card)
        else:
            return _list(directory, wild_card)

    @classmethod
    def remove_invalid_filename_characters(cls, filename: str) -> str:
        """Returns the filename without characters that are invalid on a file system.

        Parameters
        ----------
        filename: string that has to be converted to a string without invalid characters

        Returns
        -------
        String that can be used to create a file with
        """

        return re.sub(r"[-:@%^&<>|'`,;=()!\[\]\"\"\"\".*?\\\/]+", r"", filename)

    def upload_file(self, local_file: str, remote_file: str, overwrite: bool = True):
        """Copies a file from the local system to the remote system running the test.

        Parameters
        ----------
        local_file : path to the local file location
        remote_file: path on the remote system to copy the file to
        overwrite: if true function will overwrite the file if exist
        """
        assert not (self.file_exists(remote_file) and not overwrite), "File already exists and overwrite set to False"

        if self.file_exists(remote_file) and overwrite:
            self.delete_file(remote_file)
        # empty files are not created so create the file via createTextFile call
        if os.path.getsize(local_file) == 0:
            self.connection.createTextFile(remote_file, "")
        self.connection.upload(local_file, remote_file)

    def upload_directory(self, local_directory: str, remote_directory: str, wild_card: str, overwrite: bool):
        """Copies a directory (including subdirectories) to the remote system.

        Parameters
        ----------
        local_directory: local directory to copy
        remote_directory: location to copy the directory to
        wild_card: Wildcard to select a specific set of files
        overwrite: if true function will overwrite the file if exist
        """
        local_files = [str(file_path) for file_path in pathlib.Path(local_directory).rglob(wild_card)]
        for local_file in local_files:
            remote_dir = FileUtils._get_remote_path_name(local_file, local_directory, remote_directory)
            remote_file = FileUtils._get_remote_filename(local_file, remote_dir)
            # create path
            self.create_directory(remote_dir)
            self.upload_file(local_file, remote_file, overwrite)

    @staticmethod
    def _get_remote_filename(local_file, remote_dir):
        return os.path.join(remote_dir, os.path.basename(local_file))

    @staticmethod
    def _get_remote_path_name(local_file, local_directory, remote_directory):
        # create remote path
        remote_file_directory_part = os.path.dirname(local_file).replace(local_directory, "").strip("\\")
        return os.path.join(remote_directory, remote_file_directory_part)

    @classmethod
    def get_directory_hash(cls, local_directory: str, wild_card: str, recursive=True) -> str:
        """Creates hash on files combined content in given directory.

        Parameters
        ----------
        local_directory: local directory to search for given wildcard
        wild_card: Wildcard to select a specific set of files
        recursive: States if the function should also check sub-directories of the given directory

        Returns
        -------
        Hash as a string
        """
        if not recursive:
            files = pathlib.Path(local_directory).glob(wild_card)
        else:
            files = pathlib.Path(local_directory).rglob(wild_card)

        blake2b_hash = hashlib.blake2b()
        for file_path in files:
            blake2b_hash.update(open(file_path, "rb").read())

        return blake2b_hash.hexdigest()

    def download_file(self, remote_file: str, local_file: str, overwrite: bool):
        """

        Parameters
        ----------
        remote_file: Source path to the remote file location
        local_file: Target path to the local file location
        overwrite: if true function will overwrite the target file if exist
        """
        assert self.file_exists(remote_file), "Remote file does not exist"
        assert not (
            os.path.exists(local_file) and not overwrite
        ), "Local file already exists and overwrite set to False"
        if os.path.exists(local_file) and overwrite:
            os.remove(local_file)
        self.connection.download(remote_file, local_file)

    def create_text_file(self, remote_file: str, text: str, overwrite: bool = False):
        """

        Parameters
        ----------
        remote_file: Path to the remote file location where to create the text file to
        text: Content of the file
        overwrite: if true function will overwrite the text file if exist
        """
        assert not (self.file_exists(remote_file) and not overwrite), "File already exists and overwrite set to False"
        if overwrite and self.file_exists(remote_file):
            self.delete_file(remote_file)
        self.connection.createTextFile(remote_file, text)

    def delete_files(self, remote_directory: str, wild_card: str, recursive: bool = True, log_delete: bool = False):
        """Deletes all files matching the wildcard from a given remote directory.

        Parameters
        ----------
        remote_directory: Folder to remove files from
        wild_card: Type of files to delete
        recursive: States if the function should also check sub-directories of the given directory
        log_delete: Determines whether to log the files being deleted or not
        """
        assert self.directory_exists(remote_directory), "Folder to delete files from does not exist"
        for filename in self.get_directory_content(remote_directory, wild_card, recursive):
            if self.file_exists(filename):
                if log_delete:
                    test.log(f"Deleting file: {filename}")
                self.delete_file(filename)

    def download_files(self, remote_directory: str, local_directory: str, wild_card: str, recursive=True):
        """Download all files matching the wildcard from a given remote directory to the local directory.

        Parameters
        ----------
        remote_directory: Remote folder to download files from
        local_directory: Local folder to download files from
        wild_card: Type of files to delete
        recursive: States if the function should also check sub-directories of the given directory
        """
        assert self.directory_exists(remote_directory), "Folder to download files from does not exist"

        for remote_file_path in self.get_directory_content(remote_directory, wild_card, recursive):
            if self.file_exists(remote_file_path):
                file_path_basename = os.path.basename(remote_file_path)
                local_file_path = os.path.join(local_directory, file_path_basename)
                self.download_file(remote_file_path, local_file_path, True)
                test.attachFile(
                    os.path.join(local_directory, file_path_basename),
                    f"Created following csv-file during this run: [{local_file_path}]",
                )

    def delete_read_only_files(self, remote_directory: str, wild_card: str, recursive=True):
        """Deletes all files matching the wildcard from a given remote directory.

        Parameters
        ----------
        remote_directory: Folder to remove files from
        wild_card: Type of files to delete
        recursive: States if the function should also check sub-directories of the given directory
        """
        assert self.directory_exists(remote_directory), "Folder to delete files from does not exist"
        for filename in self.get_directory_content(remote_directory, wild_card, recursive):
            if self.file_exists(filename):
                self.delete_read_only_file(filename)

    @staticmethod
    def get_latest_file(directory: str, wildcard: str = "*.*") -> str:
        """Gets the latest file from a directory.

        Parameters
        ----------
        directory: Directory to search
        wildcard: Wildcard to set for searching, default is all files

        Returns
        -------
        Full filename of the latest file found, empty string if no file was found
        """
        list_of_files = glob.glob(f"{directory}/{wildcard}")
        latest_file_path = max(list_of_files, key=os.path.getctime)
        if not latest_file_path:
            return ""
        return latest_file_path

    @staticmethod
    def get_unique_filename(prefix: str = "", suffix: str = "") -> str:
        asctime = remove_chars(datetime.datetime.now().isoformat(), '\\/:*?"<>|')
        return f"{prefix}{asctime}{suffix}"

    def get_file_size(self, file_path: str) -> int:
        """Gets the size of the given file.

        Parameters
        ----------
        file_path: path of the file to get the size of

        Returns
        -------
        the size of the file in bytes
        """
        args = ["powershell", f"(Get-Item -Path '{file_path}').Length"]
        (exitcode, stdout, stderr) = self.connection.execute(args)
        if exitcode != "0":
            test.fail(f"Unable to get file size of '{file_path}'\nstdout: {stdout}\nstderr: {stderr}")
        else:
            return int(stdout.strip())

    @staticmethod
    def compare_csv_files(file1_path, file2_path):
        with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
            file1_content = [line.strip().split(",") for line in file1.readlines()]
            file2_content = [line.strip().split(",") for line in file2.readlines()]
            return file1_content == file2_content


class RemoteFile:
    def __init__(self, *args, **kwargs):
        self.remote_file_path = remote_path(args[0])
        _, file_name = os.path.split(self.remote_file_path)
        local_file_name = "copy-" + file_name
        self.local_file_path = os.path.join(tempfile.gettempdir(), local_file_name)
        FileUtils().download_file(self.remote_file_path, self.local_file_path, overwrite=True)
        self.file_object = open(self.local_file_path, *args[1:], **kwargs)

    def read(self, *args, **kwargs):
        return self.file_object.read(*args, **kwargs)

    def seek(self, *args, **kwargs):
        return self.file_object.seek(*args, **kwargs)

    def tell(self, *args, **kwargs):
        return self.file_object.tell(*args, **kwargs)

    def close(self, *args, **kwargs):
        return self.file_object.close(*args, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()
        os.remove(self.local_file_path)


class ImageFile(RemoteFile):
    """An image file in the AUT host.

    It can handle MRC files and all the file types supported by the PIL library.
    """

    @property
    def type(self) -> str:
        """Returns the type of the image file.

        Returns
        -------
        The type of the image file
        """
        return self.local_file_path.split(".")[-1]

    @property
    def image_size(self) -> Tuple[int, int]:
        """Returns the size of the image file.

        Returns
        -------
        The size of the image file as a tuple (width, height).
        """
        if self.type == "mrc":
            with mrcfile.open(self.local_file_path) as mrc:
                image_height, image_width = mrc.data.shape
                return image_width, image_height
        elif self.type == "svg":
            return find_svg_image_size(self.local_file_path)
        else:
            try:
                with Image.open(self.local_file_path) as image:
                    return image.size
            except UnidentifiedImageError as e:
                test.fail("Cannot open file %s: Reason: %s" % (self.local_file_path, e))


def remote_path(path: str) -> str:
    """Converts a path to a remote path.

    This is useful when we want a path from the remote system that contains a
    variable like %TEMP%. In this case, this variable will be replaced by the
    temporary directory of the remote system.

    Parameters
    ----------
    path: Path to convert

    Returns
    -------
    The remote path.
    """

    file_utils = FileUtils()

    if "%TEMP%" in path.upper():
        path = path.replace("%TEMP%", file_utils.get_remote_temp_dir())

    return path


def readline_reverse(filename: str) -> str:
    """Reads lines starting at the end of the file.

    Parameters
    ----------
    filename: Name of the file to read

    Returns
    -------
    Line read from file
    """
    with RemoteFile(filename, "rt") as qfile:
        qfile.seek(0, os.SEEK_END)
        position = qfile.tell()
        line = ""
        while position >= 0:
            qfile.seek(position)
            next_char = qfile.read(1)
            if next_char == "\n":
                yield line[::-1]
                line = ""
            else:
                line += next_char
            position -= 1
        yield line[::-1]


def local_update_ini_file(ini_file: str, ini_configurations: dict):
    """Modify specific configurations parameters on the given local ini file and log changes done.

    Parameters
    ----------
    ini_file: Full path of the ini file
    ini_configurations: Dictionary of configurations to be replaced on the ini file
    """
    local_log_path = os.path.join(tempfile.gettempdir(), "velox_ini_values_found_log.txt")
    log_values_found = ""
    with open(ini_file, "r") as reading_file:
        new_file_content = ""
        for line in reading_file:
            stripped_line = line.strip()
            new_line = ""
            for key, value in ini_configurations.items():
                key_line = stripped_line.split("=")[0]
                if key == key_line:
                    log_values_found += f"Found [{stripped_line}] configuration and changed it to [{value}]\n"
                    new_line = key + "=" + value
                    new_file_content += new_line + "\n"

            if new_line == "":
                new_file_content += stripped_line + "\n"

    with open(ini_file, "w") as writing_file:
        writing_file.write(new_file_content)

    with open(local_log_path, "w") as writing_file:
        writing_file.write(log_values_found)
    test.attachFile(local_log_path)
    log_attached_file("Velox.ini log of values found", os.path.basename(local_log_path))


def update_ini_file(ini_relative_path: str, ini_configurations: dict):
    """Modify specific configurations parameters on an ini file.

    Parameters
    ----------
    ini_relative_path: Full path of the ini file
    ini_configurations: Dictionary of configurations to be replaced on the ini file
    """
    file_utils = FileUtils()
    roaming_path = file_utils.connection.getEnvironmentVariable("APPDATA")
    velox_ini_file = os.path.join(roaming_path, ini_relative_path)
    local_file_path = os.path.join(tempfile.gettempdir(), os.path.basename(velox_ini_file))
    file_utils.download_file(velox_ini_file, local_file_path, overwrite=True)
    test.attachFile(local_file_path)
    log_attached_file("Previous Velox.ini file", os.path.basename(local_file_path))
    local_update_ini_file(local_file_path, ini_configurations)
    file_utils.upload_file(local_file_path, velox_ini_file)
