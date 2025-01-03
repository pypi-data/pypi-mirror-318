# Copyright(c) 2021-2022 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import os
from remotesystem import RemoteSystem

from utils.string_utils import remove_suffix


class Process:
    def __init__(self, connection=RemoteSystem()):
        self.connection = connection

    def get_process_ids(self, process_name) -> list:
        """Get the process ids for the given process name.

        Parameters
        ----------
        process_name: name of the process to get the process id from

        Returns
        -------
        List of process ids as list of strings
        """

        return self._get_process_ids(process_name)

    def start(self, args, remote_working_dir: str = None, env: dict = None, options: dict = None):
        """Start the process on the remote system.

        Parameters
        ----------
        args: list/array of the command and all parameters
        remote_working_dir: working directory for executing the provided command
        env: allows to set or remove environment variables.
            To remove an environment variable use an empty string as value
        options:parameter offers additional, sometimes less often used options.
            options.keepLineEnding
                Type: Boolean
                Default: True
                If provided and set to false, line endings in stdout/stderr output of the started process will be
                converted to '\n' (Unix) newlines.
            options.clearenv
                Type: Boolean
                Default: False
                If provided and set to true, the process will be started with a minimal environment.
                However, on most OS it is not possible to remove all environment variables because then some
                functionality or tools provided by the operating system would not work any more.
            options.timeout
                Type: Integer
                Default: 30
                Value is a timeout in seconds. It is used to limit the execution time of the started process.
            options.encoding
                Type: String
                Default: UTF-8
                Name of the encoding of the stdout/stderr output of the started process.
                See below for a list of supported encodings.

        Returns
        -------
            (exitcode, stdout, stderr)
        """
        return self.connection.execute(args, remote_working_dir, env, options)

    def is_running(self, process_name: str, process_location: str = None) -> bool:
        """Returns True if the given process is running on the remote system.

        Parameters
        ----------
        process_name: Name of the process can be with or without .exe suffix
        process_location: Optional parameter when a executable in a specific location needs to be checked

        Returns
        -------
        bool:
            True if the process_name and process_location is found in the list of processes on the remote system
        """
        return len(self._get_process_ids(process_name, process_location)) != 0

    def kill(self, process_name: str, process_location: str = None) -> bool:
        """Returns True if the given process is running on the remote system.

        Parameters
        ----------
        process_name: Name of the process can be with or without .exe suffix
        process_location: Optional parameter when a executable in a specific location needs to be killed

        Returns
        -------
        bool:
            True if the process_name was found and killed
        """
        process_ids = self._get_process_ids(process_name, process_location)
        if not len(process_ids):
            return False
        for pid in process_ids:
            self.kill_with_pid(pid)
        return True

    def kill_with_pid(self, process_id: str):
        """Kills the process with the given process id.

        Parameters
        ----------
        process_id: Process id
        """
        args = ["taskkill", "/f", "/pid", "{}".format(process_id)]
        (exitcode, stdout, stderr) = self.connection.execute(args)
        assert exitcode == "0", f"Unable to kill process {process_id}: {stderr}"

    def _get_process_list(self):
        """Creates a list of process as a csv with the following format "Process-name", "Path to executable", "Process
        Id".

        Returns
        -------
        csv list with line-format "Process-name", "Path to executable", "Process Id"
        """
        # get processes as csv-list with name, location, pid
        args = [
            "powershell.exe ",
            "-command",
            "Invoke-Expression",
            '"Get-Process',
            "|",
            "Select-Object",
            "-Property",
            "Name",
            ",",
            "Path",
            "," "Id",
            "|",
            "ConvertTo-CSV",
            '-NoTypeInformation"',
        ]
        (exitcode, stdout, stderr) = self.start(args)
        assert exitcode == "0", f"Unable to retrieve list of processes from the remote system: {stderr}"
        return stdout

    def _get_process_ids(self, process_name: str, process_location: str = None) -> list:
        process_ids = []
        process_name = process_name.lower()
        for line in self._get_process_list().splitlines():
            split_arr = [item.lower().strip('"') for item in line.split(",")]
            if remove_suffix(process_name, ".exe") == split_arr[0] and (
                not process_location or os.path.join(process_location.lower(), process_name) == split_arr[1]
            ):
                process_ids.append(split_arr[2])
        return process_ids
