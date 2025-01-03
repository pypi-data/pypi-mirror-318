# Copyright(c) 2022-2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import os
import tempfile

from common.environment import Environment
from common.execution_info import squish_root_folder
from common.file_utils import FileUtils
from common.process import Process
from common.squish_info import get_squish_python3_directory


class ServerInstaller:
    srpc = "Srpc"
    environment = Environment()
    local_srpc_folder = os.path.join(squish_root_folder(), "framework", srpc)
    squish_version = environment.get_remote_environment_variable("squish_version", "")
    remote_server_dir = os.path.join(
        environment.get_remote_environment_variable("TEMP"), "Squish", squish_version, "RPCServer"
    )
    remote_virtual_env_dir = os.path.join(remote_server_dir, "venv")
    remote_srpc_dir = os.path.join(remote_server_dir, "framework", srpc)
    remote_scripts_dir = os.path.join(remote_virtual_env_dir, "Scripts")
    hash_filename = "hash.blake2b"
    remote_hash_file_copy = os.path.join(tempfile.gettempdir(), hash_filename)
    remote_hash_file = os.path.join(remote_srpc_dir, hash_filename)
    squish_python = os.path.join(get_squish_python3_directory(), "python.exe")
    local_requirements_file_path = os.path.join(squish_root_folder(), "requirements_server.txt")
    remote_requirements_file_path = os.path.join(remote_virtual_env_dir, "requirements_server.txt")
    file_wildcard = "*.*"

    def __init__(self, file_utils=FileUtils(), process=Process()):
        self.file_utils = file_utils
        self.process = process

    def install_server(self):
        if not self._virtual_env_exists():
            self._create_virtual_env()
        if self._server_files_changed():
            self.stop_server()
            self._remove_server_files()
            self._copy_server_files()
            self._add_hash_to_remote()
        if not self._server_started():
            self._activate_virtual_env()
            self._start_server()

    def stop_server(self):
        self.process.kill("python.exe", self.remote_scripts_dir)

    def _virtual_env_exists(self) -> bool:
        return self.file_utils.directory_exists(self.remote_virtual_env_dir)

    def _server_files_changed(self) -> bool:
        if self.file_utils.file_exists(self.remote_hash_file):
            # get remote hash
            self.file_utils.download_file(self.remote_hash_file, self.remote_hash_file_copy, True)
            remote_hash = open(self.remote_hash_file_copy, "rt").read()
            local_hash = FileUtils.get_directory_hash(self.local_srpc_folder, self.file_wildcard)
            return remote_hash != local_hash
        return True

    def _add_hash_to_remote(self):
        local_hash = self.file_utils.get_directory_hash(self.local_srpc_folder, self.file_wildcard)
        self.file_utils.create_text_file(self.remote_hash_file, local_hash, True)

    def _server_started(self) -> bool:
        return self.process.is_running("python.exe", self.remote_scripts_dir)

    def _create_virtual_env(self):
        self._upgrade_pip()
        self._upgrade_virtual_env()
        self.__create_virtual_env()

    def __create_virtual_env(self):
        args = [self.squish_python, "-m", "venv", self.remote_virtual_env_dir]
        (exitcode, _, _) = self.process.start(args)
        assert exitcode == "0", "Unable to execute create virtualenv command"

    def _upgrade_virtual_env(self):
        args = [self.squish_python, "-m", "pip", "install", "--upgrade", "virtualenv"]
        (exitcode, _, stderr) = self.process.start(args)
        assert exitcode == "0", f"Unable to execute upgrade virtualenv command: {stderr}"

    def _upgrade_pip(self):
        args = [self.squish_python, "-m", "pip", "install", "--upgrade", "pip"]
        (exitcode, _, stderr) = self.process.start(args)
        assert exitcode == "0", f"Unable to execute upgrade pip command: {stderr}"

    def _copy_server_files(self):
        self.file_utils.upload_directory(self.local_srpc_folder, self.remote_srpc_dir, self.file_wildcard, True)

    def _activate_virtual_env(self):
        # copy virtual env requirements to remote system
        self.file_utils.upload_file(self.local_requirements_file_path, self.remote_requirements_file_path)

        # activate the remote virtual env
        args = [os.path.join(self.remote_scripts_dir, "activate.bat")]
        (exitcode, _, _) = self.process.start(args)
        assert exitcode == "0", "Unable to activate virtualenv"

        # install the remote requirements
        args = [os.path.join(self.remote_scripts_dir, "pip"), "install", "-r", self.remote_requirements_file_path]
        (exitcode, _, _) = self.process.start(args)
        assert exitcode == "0", "Unable to add the required modules to the virtualenv"

    def _start_server(self):
        python_exe = os.path.join(self.remote_scripts_dir, "python.exe")
        server_py = os.path.join(self.remote_srpc_dir, "server.py")
        args = ["cmd", "/c", python_exe, server_py]
        # due to the command starting a separate process no need to wait for the default timeout
        (exitcode, _, _) = self.process.start(args, self.remote_srpc_dir, options={"timeout": 1})

    def _remove_server_files(self):
        if self.file_utils.directory_exists(self.remote_srpc_dir):
            self.file_utils.delete_files(self.remote_srpc_dir, self.file_wildcard, True)
