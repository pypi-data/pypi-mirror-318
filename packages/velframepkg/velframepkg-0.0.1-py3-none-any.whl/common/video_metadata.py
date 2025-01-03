# Copyright(c) 2023-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

import os
import re
import squish
import test
from remotesystem import RemoteSystem
from typing import Tuple

from common import Environment, FileUtils

UPLOAD_FILE_TIMEOUT = 5000


class VideoMetadata:
    def __init__(self, video_file: str, connection=RemoteSystem()):
        self.__video_file = video_file
        self.__connection = connection

        self.__upload_metadata_script()
        self.__frame_rate, self.__frame_width, self.__frame_height = self.__run_metadata_script()

    @property
    def frame_rate(self) -> int:
        return self.__frame_rate

    @property
    def frame_width(self) -> int:
        return self.__frame_width

    @property
    def frame_height(self) -> int:
        return self.__frame_height

    def __upload_metadata_script(self):
        framework_common_path = os.path.dirname(os.path.realpath(__file__))
        local_script_path = os.path.join(framework_common_path, "scripts", "video_metadata.ps1")
        self.__remote_script_path = os.path.join(
            Environment(self.__connection).get_remote_environment_variable("TEMP"),
            "Squish",
            "video_metadata.ps1",
        )
        file_utils = FileUtils(self.__connection)

        def upload_metadata_script_file(remote_script_path):
            # We use this try block as a workaround for the https://thermofisher-asg.atlassian.net/browse/VEL-45608 bug
            try:
                file_utils.upload_file(local_script_path, remote_script_path)
                return True
            except Exception as exception_message:
                test.log(f"Failed to upload metadata script file: [{exception_message}]")
                return False

        if squish.waitFor(lambda: upload_metadata_script_file(self.__remote_script_path), UPLOAD_FILE_TIMEOUT):
            test.log(f"Metadata script file was uploaded to [{self.__remote_script_path}]")
        else:
            test.fail(f"Failed to upload metadata script [{local_script_path}]")

    def __run_metadata_script(self) -> Tuple[int, int, int]:
        command = ["powershell", "-file", self.__remote_script_path, "-FilePath", self.__video_file]
        error_code, stdout, stderr = self.__connection.execute(command)
        test.log(f"command: {command}")

        if error_code != str(0):
            test.log(f"error_code: {error_code}")
            test.log(f"stderr: {stderr}")
            test.fail(f"video metadata script failed for video file {self.__video_file}")

        output_pattern = r"framerate: (\d+) framewidth: (\d+) frameheight: (\d+)"
        match = re.search(output_pattern, stdout)
        if match:
            return int(match.group(1)), int(match.group(2)), int(match.group(3))
        else:
            test.fail(f"script did not return expected output\nscript output: {stdout}")
