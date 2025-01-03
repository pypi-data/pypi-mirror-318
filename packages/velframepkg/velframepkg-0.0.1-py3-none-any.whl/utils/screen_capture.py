# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import glob
import os
import re
import shutil
import subprocess
import sys
import time

OBS_FILE_PATH = os.getenv("ObsInstallationPath", r"C:\ObsStudio")
OBS_BIN_PATH = os.path.join(OBS_FILE_PATH, "bin", "32bit")
OBS_EXECUTABLE = "obs32.exe"
OBS_FULL_PATH_EXECUTABLE = os.path.join(OBS_BIN_PATH, OBS_EXECUTABLE)

OBS_VIDEO_FILE_PATH = os.path.join(os.getenv("temp"), "ObsStudioRecordings")
SQUISH_FILE_SERVER_PATH = r"\\veloxfileserver.w2k.feico.com\velox"
SYSTEM_TEST_FILE_PATH = os.path.join(SQUISH_FILE_SERVER_PATH, "SystemTest")


def _clean_recordings_directory():
    """Clean OBS video directory."""
    if os.path.isdir(OBS_VIDEO_FILE_PATH):
        shutil.rmtree(OBS_VIDEO_FILE_PATH)
    os.mkdir(OBS_VIDEO_FILE_PATH)


def _start_obs_application():
    """Starts the OBS executable from the command line."""
    workspace_path = os.getenv("workspace")
    profile_file = os.path.join(
        workspace_path, r"\workspace\Squish\framework\utils\video\AppData\basic\profiles\MpcProfile", "basic.ini"
    )
    scene_file = os.path.join(
        workspace_path, r"\workspace\Squish\framework\utils\video\AppData\basic\scenes", "MpcScene.json"
    )

    args = [
        "cmd",
        "/c",
        "start",
        OBS_FULL_PATH_EXECUTABLE,
        "--startrecording",
        "--minimize-to-tray",
        "--disable-updater",
        "--profile",
        "--allow-opengl",
        profile_file,
        "--scene",
        scene_file,
    ]
    subprocess.run(args, cwd=OBS_BIN_PATH)


def _stop_obs_application():
    """Kills the running OBS instance, if it exists."""
    args = ["taskkill", "/F", "/IM", OBS_EXECUTABLE]
    subprocess.run(args)


def _get_local_video_filepath() -> str:
    """Gets the recorded video filepath.

    Returns
    -------
    The path to the video recorded by OBS (an empty string if it doesn't exist)
    """
    mkv_files = glob.glob(f"{OBS_VIDEO_FILE_PATH}/*.mkv")

    if len(mkv_files) == 0:
        return ""
    else:
        return mkv_files[0]


def _upload_video_to_server(test_name: str):
    """Creates the path on the Velox file server to upload the recording to (if it doesn't exist).

    Parameters
    ----------
    test_name: The name of the test to use for titling the video.

    Raises
    ------
    WindowsError if local video file is still locked by copy operation after 1 minute
    """
    local_video_filepath = _get_local_video_filepath()
    if not local_video_filepath:
        return

    local_filename_without_extension = os.path.splitext(os.path.basename(local_video_filepath))[0]
    test_name_cleaned = re.sub(r"[-:@%^&<>|'`,;=()!\[\]\"\"\"\".*?\\\/]+", "", test_name).replace(" ", "_")
    remote_filename = f"{local_filename_without_extension}_{test_name_cleaned}.mkv"

    server_video_dir_path = os.path.join(
        SYSTEM_TEST_FILE_PATH, os.getenv("job_name"), os.getenv("build_number"), "Video"
    )
    server_video_filepath = os.path.join(server_video_dir_path, remote_filename)
    if not os.path.isdir(server_video_dir_path):
        os.mkdir(server_video_dir_path)
    shutil.copy(local_video_filepath, server_video_filepath)

    # Wait for copy operation to finish and file to become unlocked
    for i in range(60):
        try:
            # check if file is still locked after copy
            os.rename(local_video_filepath, local_video_filepath)
            return
        except Exception:
            time.sleep(1)

    raise WindowsError(f"video file at {local_video_filepath} still locked")


def start_recording() -> None:
    """Starts a video recording of the screen using OBS."""
    if os.getenv("RecordSession", "false") == "true" and os.getenv("BUILD_URL"):
        _clean_recordings_directory()
        _start_obs_application()


def stop_recording(test_name: str = "squish_crash"):
    """Stops the video recording of the screen.

    Parameters
    ----------
    test_name: The name of the test to use for titling the video. Defaults to 'squish_crash'
    since this will not be possible to set when Squish crashes.
    """
    if os.getenv("RecordSession", "false") != "true" or not os.getenv("BUILD_URL"):
        return

    # sleep before closing OBS so that we can capture the last seconds of the test
    time.sleep(10)
    _stop_obs_application()
    _upload_video_to_server(test_name)
    _clean_recordings_directory()


# This file will be used as a script as part of the Jenkins job
# so that crashes still get their video recorded.
# As a script, this file can be used like:
#   .\screen_capture.py start (start recording with OBS)
#   .\screen_capture.py stop (stop recording with OBS)
if __name__ == "__main__":
    script_name = os.path.basename(os.path.realpath(__file__))
    if len(sys.argv) != 2:
        sys.exit(f"{script_name} takes only one argument ('start' or 'stop')")

    recording_mode = sys.argv[1]
    if sys.argv[1] == "start":
        start_recording()
    elif sys.argv[1] == "stop":
        stop_recording()
    else:
        sys.exit(f"The only accepted arguments for {script_name} are 'start' or 'stop'")
