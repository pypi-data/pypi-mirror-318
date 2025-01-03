# Copyright(c) 2022-2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

import os
from remotesystem import RemoteSystem

from common.environment import Environment
from common.file_utils import FileUtils


def get_squish_directory() -> str:
    """Searches for squish installation directory. Checks the user location first then Velox location (C:\\Squish) and
    finally the complete drive.

    Returns
    -------
    Directory where the squish is installed.
    """
    environment = Environment()
    home_path = os.path.join(
        environment.get_remote_environment_variable("HOMEDRIVE"),
        environment.get_remote_environment_variable("HOMEPATH"),
    )
    mpc_squish_path = environment.get_remote_environment_variable("squish_installation_path", "invalid_version")

    file_utils = FileUtils()
    if file_utils.directory_exists(mpc_squish_path):
        return mpc_squish_path
    directories = file_utils.get_directories(home_path, r"*Squish for Qt*")
    directories.sort(reverse=True)
    if directories:
        return directories[0]

    assert False, "Unable to find the squish installation directory"


def get_squish_python3_directory() -> str:
    """Returns directory where python 3.x version of squish is installed.

    Returns
    -------
    Directory where python 3.x installed
    """
    return os.path.join(get_squish_directory(), "python3")


def get_squish_version(remote_system: RemoteSystem = RemoteSystem()) -> str:
    """Gets the version of Squish used by the test execution.

    Parameters
    ----------
    remote_system: an instance of RemoteSystem for running commands

    Returns
    -------
    The version of Squish used as a string
    """
    return Environment().get_remote_environment_variable("squish_version")
