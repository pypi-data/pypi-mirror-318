# Copyright(c) 2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

import squish
import test
from remotesystem import RemoteSystem

from common import Process
from common.squish_info import get_squish_directory
from velox.labels.installer import VELOX_START_MENU_LINK
from velox.labels.velox_application import VeloxCommandLineOption


class Launcher:
    @staticmethod
    def start_velox_start_menu(context, port: int = 4444):
        """Starts velox with Windows Shortcut (Velox.lnk) using startaut.exe.

         Parameters
        ----------
        port: port on which Velox is to be started
        """
        squish_startaut_path = get_squish_directory() + "\\bin\\startaut.exe"
        test.log(f"Squish startaut path is {squish_startaut_path}")

        try:
            # Command line arguments
            args = [
                squish_startaut_path,
                "--verbose",
                f"--port={port}",
                VELOX_START_MENU_LINK,
            ]
            if "is_offline" in context.userData and context.userData["is_offline"]:
                args.append(VeloxCommandLineOption.OFFLINE.value)
            test.log("Starting velox using velox start menu")
            remote_system = RemoteSystem()
            (exitcode, _, _) = remote_system.execute(args)
            test.log(f"Velox started with exit code {exitcode}")
        except Exception as ex:
            test.warning(f"Exception occured while starting velox with startaut: {repr(ex)}")

    @staticmethod
    def start_velox_executable(context, port: int = 4444):
        """Starts velox using Velox executable using startaut.exe.

        Parameters
        ----------
        process: an instance of Process
        remote_system: an instance of RemoteSystem
        port: port on which Velox is to be started
        """

        # Kill Velox if it is already running
        process = Process()
        process.kill("Velox")

        squish_startaut_path = get_squish_directory() + "\\bin\\startaut.exe"
        test.log(f"Squish startaut path is {squish_startaut_path}")

        try:
            # Command line arguments
            args = [squish_startaut_path, "--verbose", f"--port={port}", f"{context.userData['velox_exe_path']}"]
            if "is_offline" in context.userData and context.userData["is_offline"]:
                args.append(VeloxCommandLineOption.OFFLINE.value)
            test.log("Starting velox using velox.exe")
            remote_system = RemoteSystem()
            (exitcode, _, _) = remote_system.execute(args)
            test.log(f"Velox started with exit code {exitcode}")

        except Exception as ex:
            test.warning(f"Exception occured while starting velox with startaut: {repr(ex)}")

    @staticmethod
    def add_attachable_aut_squish(context, application_alias: str, port: int = 4444):
        """Adds an application which is running on the given port number as an attachable aut to squish configurations
        with the given alias name.

        Parameters
        ----------
        remote_system: an instance of RemoteSystem
        application_alias: Alias name with which the application will be added to Squish configuration file
        port: Port number on which the application,to be linked, is running
        """

        squish_server_path = get_squish_directory() + "\\bin\\squishserver.exe"
        test.log(f"Squish server path is {squish_server_path}")

        args = [squish_server_path, "--verbose", "--config", "addAttachableAUT", f"{application_alias}", f"{port}"]
        test.log("Adding AttachableAut to Squish configuration")
        remote_system = RemoteSystem()
        (exitcode, _, _) = remote_system.execute(args)

        if exitcode == "0":
            test.log(f"{application_alias} successfully added to AttachableAUTs list under Squish configurations")
            ctx = squish.attachToApplication(application_alias)
            context.userData["attachable_aut"] = application_alias
            context.userData["port"] = port
            context.userData["application"] = ctx
        else:
            test.fail("Unable to add attachable aut to squish configurations")

    @staticmethod
    def remove_attachable_aut_squish(application_alias: str, port: int = 4444):
        """Remove an application which is running on the given port number as an attachable aut to squish configurations
        with the given alias name.

        Parameters
        ----------
        remote_system: an instance of RemoteSystem
        application_alias: Alias name for the application which should be removed from Squish configuration file
        port: Port number on which the application,to be linked, is running
        """
        squish_server_path = get_squish_directory() + "\\bin\\squishserver.exe"
        test.log(f"Squish server path is {squish_server_path}")

        args = [squish_server_path, "--config", "removeAttachableAUT", f"{application_alias}", f"{port}"]
        test.log("Removing Attachable Aut to squish configuration")
        remote_system = RemoteSystem()
        (exitcode, _, _) = remote_system.execute(args)

        if exitcode == "0":
            test.log(f"{application_alias} successfully removed from AttachableAUTs list under squish configurations")
        else:
            test.warning("Unable to remove attachable aut to squish configurations")

    @staticmethod
    def start_velox_second_instance(context):
        """Starts a 2nd instance of Velox.

        Parameters
        ----------
        remote_system: an instance of RemoteSystem
        """
        try:
            # Command line arguments
            args = [f"{context.userData['velox_exe_path']}"]
            if "is_offline" in context.userData and context.userData["is_offline"]:
                args.append(VeloxCommandLineOption.OFFLINE.value)
            test.log("Starting 2nd instance of velox using velox.exe")
            remote_system = RemoteSystem()
            (exitcode, _, _) = remote_system.execute(args)
            test.log(f"Velox started with exit code {exitcode}")
        except Exception as ex:
            test.warning(f"Exception occured while starting velox: {repr(ex)}")
