# Copyright(c) 2020-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
from remotesystem import RemoteSystem


class RegistryContent:

    _not_fnd_message = "ERROR: The system was unable to find the specified registry key or value."

    def __init__(self, key):
        self._key = key
        self._id_value_map = None
        self._list = None
        self._exists = None

    @property
    def dict(self) -> dict:
        """Returns content as a dictionary based the configuration found in the registry.

        Returns
        -------
        dictionary with registry name as key and data as value
        """
        if not self._id_value_map:
            self._id_value_map = self._create_mapping(self.list)
        return self._id_value_map

    @property
    def exists(self) -> bool:
        """Returns if the key exists.

        Returns
        -------
        True if exist
        """
        if not self._exists:
            remote = RemoteSystem()
            args = ["reg", "query", self._key]
            (exitcode, stdout, _) = remote.execute(args)
            self._exists = self._not_fnd_message not in stdout
            if not self._exists:
                # the registry key does not exists set the list to empty
                self._list = []
        return self._exists

    @property
    def list(self) -> list:
        """Returns content of registry as a list of strings.

        Returns
        -------
        List of strings
        """
        if (not self._list) and self.exists:
            remote = RemoteSystem()
            args = ["reg", "query", self._key]
            (exitcode, stdout, _) = remote.execute(args)
            self._list = stdout.strip().split("\n")
        return self._list

    def _create_mapping(self, reg_lines: list) -> dict:
        """Converts the registry lines list into a dictionary.

        Parameters
        ----------
        reg_lines: List of registry names, types and values

        Returns
        -------
        Dictionary of the registry variables in _key
        """
        id_value_map = {}
        if self._key in reg_lines[0]:
            reg_lines = reg_lines[1:]
        for line in iter(reg_lines):
            line = line.strip()
            split_arr = line.split("REG_SZ")
            if len(split_arr) == 1:
                split_arr = line.split("REG_DWORD")
            if len(split_arr) > 1:
                id_value_map[split_arr[0].strip()] = split_arr[1].strip()
        return id_value_map

    def _export(self, file_path: str) -> bool:
        """Copies the specified subkeys, entries, and values of the local computer into a file.
        Run the windows cmd : reg export self._key <file_path> /y
        See: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-export

        Parameters
        ----------
        file_path: Specifies the name and path of the file to be created during the operation.

        Returns
        -------
        True if the export happen without errors. False instead.
        """
        remote = RemoteSystem()
        args = ["reg", "export", self._key, file_path, "/y"]
        (exitcode, _, _) = remote.execute(args)
        return exitcode == "0"
