# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import ctypes
import test
from remotesystem import RemoteSystem

from utils.labels.system_environment import TestSystemMapping

REGISTRY_TYPES = ["REG_SZ", "REG_MULTI_SZ", "REG_EXPAND_SZ", "REG_DWORD", "REG_QWORD", "REG_BINARY", "REG_NONE"]


class Environment:
    def __init__(self, connection=RemoteSystem()):
        self.connection = connection

    @property
    def hostname(self) -> str:
        """Returns the hostname of the system hosting the AUT.

        Returns
        -------
        Returns the hostname of the system hosting the AUT.
        """
        exitcode, hostname, stderr = self.connection.execute(["hostname"])
        if exitcode != "0":
            raise RuntimeError(
                f"An error occurred when trying to get the hostname. " f"(exitcode: {exitcode}, stderr: {stderr})"
            )
        hostname = str(hostname).strip()
        return hostname

    def get_remote_environment_variable(self, environment_variable: str, default: str = None) -> str:
        """Returns the value for the given environment variable on the AUT
        If the environment variable can't be found on the AUT the local system is checked for the given variable

        Parameters
        ----------
        environment_variable: Environment variable to retrieve value of
        default: Value if the environment variable could not be retrieved

        Returns
        -------
        # Returns remote system environment variable. If not defined (empty string) the default value is returned
        """
        try:
            remote_environment_variable = self.connection.getEnvironmentVariable(environment_variable)
            if remote_environment_variable == "":
                return default
            return remote_environment_variable
        except Exception:
            return default

    def get_str_remote_environment_variable(self, environment_variable: str, default: str = ""):
        try:
            remote_environment_variable = self.connection.getEnvironmentVariable(environment_variable)
            if remote_environment_variable == "":
                return default
            return remote_environment_variable
        except Exception:
            return default

    def get_registry_value(self, registry_path: str, registry_key: str) -> str:
        """Returns the value for the given registry key
        If the registry key can't be found an empty string is returned

        Parameters
        ----------
        registry_path: path to the registry location
        registry_key: key to get retrieve value from located at given registry path

        Returns
        -------
        # Returns registry value if not found an empty string
        """

        args = ["reg", "query", registry_path, r"/v", registry_key]
        (exit_code, registry_value, stderr) = self.connection.execute(args)
        for registry_type in REGISTRY_TYPES:
            if registry_type in registry_value:
                reg_value_split = registry_value.split(registry_type)
                return reg_value_split[1].strip()
        return ""

    def get_system_configuration_name(self) -> str:
        """Gets the user-friendly name of a system as defined in the system config file.
        If no user-friendly name is known it will return the windows name.

        Returns
        -------
        User friendly name as a string
        """
        system_name = self.hostname
        if system_name in TestSystemMapping:
            system_name = TestSystemMapping[system_name]
        test.log(f"Found system name {system_name}")
        return system_name

    @property
    def screen_resolution(self):
        user32 = ctypes.windll.user32
        screen_resolution = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        return screen_resolution
