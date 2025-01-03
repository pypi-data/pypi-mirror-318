# Copyright(c) 2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.

import json
import os
import squish
import test
from typing import Union

from common.file_utils import FileUtils, readline_reverse
from utils.mathematical_tools import float_isclose
from utils.string_utils import convert_si_unit_to_float
from velox.configuration import MicroscopeConfiguration
from velox.labels.performance import PerformanceProfilerType


class PerformanceRunIdentifier:
    def __init__(
        self,
        test_name: str,
        width: int,
        height: int,
        number_frames: int,
    ):
        self.test_name = test_name
        self.width = width
        self.height = height
        self.number_frames = number_frames
        self.aborted = False


class StemPerformanceRunIdentifier(PerformanceRunIdentifier):
    def __init__(
        self,
        test_name: str,
        dwell_time: str,
        width: int,
        height: int,
        magnification: int,
        number_elements: int = 0,
        number_frames: int = 0,
        number_detectors: int = 0,
    ):
        super().__init__(test_name, width, height, number_frames)
        self.dwell_time = convert_si_unit_to_float(dwell_time)
        self.number_elements = number_elements
        self.magnification = magnification
        self.number_detectors = number_detectors


class CameraPerformanceRunIdentifier(PerformanceRunIdentifier):
    def __init__(
        self,
        test_name: str,
        exposure_time: str,
        width: int,
        height: int,
        image_size: int,
        number_frames: int = 0,
        binning: str = None,
        readout_name: str = None,
    ):
        super().__init__(test_name, width, height, number_frames)
        self.exposure_time = convert_si_unit_to_float(exposure_time)
        self.image_size = image_size
        self.binning = binning
        self.readout_name = readout_name


class ProfilerData:
    def __init__(
        self,
        run_identifier: Union[PerformanceRunIdentifier, StemPerformanceRunIdentifier, CameraPerformanceRunIdentifier],
        json_data: str = None,
    ):
        self._microscope_configuration = MicroscopeConfiguration()
        self.run_identifier = run_identifier
        if json_data:
            self.__dict__ = json.loads(json_data)

    @property
    def valid(self) -> bool:
        """Performance validation but always False because no actual line has been found when a nonspecific Profiler
        Data is used.

        Returns
        -------
        Always False because no actual line has been found
        """
        return False


class StemSeriesProfilerData(ProfilerData):
    @property
    def valid(self) -> bool:
        """Performance validation of the STEM Series. Verifies if all STEM Series settings values match the expected
        values defined in the identifier.

        Returns
        -------
        If all verifications pass return True else False
        """
        try:
            test.log("Checking validity all items should match")
            test.log(f"dwell_time: [{self.run_identifier.dwell_time}] == [{self.ScanParameters['DwellTime']}]")
            test.log(f"frames: [{self.run_identifier.number_frames}] == [{self.ScanParameters['FramesRequested']}]")
            test.log(f"width: [{self.run_identifier.width}] == [{self.ScanParameters['Image']['Width']}]")
            test.log(f"height: [{self.run_identifier.height}] == [{self.ScanParameters['Image']['Height']}]")
            test.log(f"#detectors: [{self.run_identifier.number_detectors}] == [{self.ScanParameters['NrDetectors']}]")
        except Exception as ex:
            test.warning(f"Exception of type [{ex.__class__.__name__}] triggered. Arguments [{ex.args}]")
            return False

        dwell_time_comparison = float_isclose(self.run_identifier.dwell_time, float(self.ScanParameters["DwellTime"]))
        frame_number_comparison = self.run_identifier.number_frames == int(self.ScanParameters["FramesRequested"])
        image_width_comparison = self.run_identifier.width == int(self.ScanParameters["Image"]["Width"])
        image_height_comparison = self.run_identifier.height == int(self.ScanParameters["Image"]["Height"])
        number_detectors_comparison = self.run_identifier.number_detectors == int(self.ScanParameters["NrDetectors"])

        return all(
            (
                dwell_time_comparison,
                frame_number_comparison,
                image_width_comparison,
                image_height_comparison,
                number_detectors_comparison,
            )
        )


class SiProfilerData(ProfilerData):
    @property
    def valid(self) -> bool:
        """Performance validation of the SI (Spectrum Imaging). Verifies if all SI settings values match the expected
        values defined in the identifier.

        Returns
        -------
        If all verifications pass return True else False
        """
        try:
            test.log("Checking validity all items should match")
            number_elements_fnd = len(self.SpectrumImagingParameters["SelectedElements"])
            test.log(f"dwell_time: {self.run_identifier.dwell_time} == {self.ScanParameters['DwellTime']}")
            test.log(f"frames: {self.run_identifier.number_frames} == {self.ScanParameters['FramesRequested']}")
            test.log(f"width: {self.run_identifier.width} == {self.ScanParameters['Image']['Width']}")
            test.log(f"height: {self.run_identifier.height} == {self.ScanParameters['Image']['Height']}")
            test.log(f"number_elements: {self.run_identifier.number_elements} == {number_elements_fnd}")
        except Exception as ex:
            test.warning(f"Exception of type [{ex.__class__.__name__}] triggered. Arguments [{ex.args}]")
            return False
        dwell_time_comparison = float_isclose(self.run_identifier.dwell_time, float(self.ScanParameters["DwellTime"]))
        frame_number_comparison = self.run_identifier.number_frames == int(self.ScanParameters["FramesRequested"])
        image_width_comparison = self.run_identifier.width == int(self.ScanParameters["Image"]["Width"])
        image_height_comparison = self.run_identifier.height == int(self.ScanParameters["Image"]["Height"])
        number_detectors_comparison = self.run_identifier.number_elements == number_elements_fnd

        test.log("Checking validity results")
        test.log(f"dwell_time: {dwell_time_comparison}")
        test.log(f"frames: {image_height_comparison}")
        test.log(f"width: {frame_number_comparison}")
        test.log(f"height: {image_width_comparison}")
        test.log(f"number_elements: {number_detectors_comparison}")

        return all(
            (
                dwell_time_comparison,
                image_height_comparison,
                frame_number_comparison,
                image_width_comparison,
                number_detectors_comparison,
            )
        )


class CameraProfilerData(ProfilerData):
    @property
    def valid(self) -> bool:
        """Performance validation of the Camera. Verifies if all Camera settings values match the expected values
        defined in the identifier.

        Returns
        -------
        If all verifications pass return True else False
        """
        try:
            width = int(self.CameraParameters["ReadOutArea"]["Right"]) - int(
                self.CameraParameters["ReadOutArea"]["Left"]
            )
            height = int(self.CameraParameters["ReadOutArea"]["Bottom"]) - int(
                self.CameraParameters["ReadOutArea"]["Top"]
            )
            test.log("Checking validity all items should match")
            test.log(f"width: {self.run_identifier.width} == {width}")
            test.log(f"height: {self.run_identifier.height} == {height}")
            test.log(f"exposure_time: {self.run_identifier.exposure_time} == {self.CameraParameters['ExposureTime']}")
            test.log(f"binning: {self.run_identifier.binning} == {self.CameraParameters['Binning']['X']}")
        except Exception as ex:
            test.warning(f"Exception of type [{ex.__class__.__name__}] triggered. Arguments [{ex.args}]")
            return False
        image_width_comparison = self.run_identifier.width == width
        image_height_comparison = self.run_identifier.height == height
        binning_comparison = int(self.run_identifier.binning) == int(self.CameraParameters["Binning"]["X"])

        if self.run_identifier.exposure_time:
            exposure_time_comparison = float_isclose(
                self.run_identifier.exposure_time, float(self.CameraParameters["ExposureTime"]), rel_tol=1e-02
            )
        else:
            exposure_time_comparison = True

        return all((image_width_comparison, image_height_comparison, exposure_time_comparison, binning_comparison))


class StemProfilerData(ProfilerData):
    @property
    def valid(self) -> bool:
        """Performance validation of the STEM. Verifies if all STEM settings values match the expected values defined in
        the identifier.

        Returns
        -------
        If all verifications pass return True else False
        """
        try:
            test.log("Checking validity all items should match")
            test.log(f'dwell_time: {self.run_identifier.dwell_time} == {self.ScanParameters["DwellTime"]}')
            test.log(f'frames: {self.run_identifier.number_frames} == {self.ScanParameters["FramesRequested"]}')
            test.log(f'width: {self.run_identifier.width} == {self.ScanParameters["Image"]["Width"]}')
            test.log(f'height: {self.run_identifier.height} == {self.ScanParameters["Image"]["Height"]}')
        except Exception as ex:
            test.warning(
                f"Exception of type [{ex.__class__.__name__}] triggered. Arguments [{ex.args}]. "
                f"Unable to determine the number of elements in the SpectrumImagingParameters"
            )
            return False

        dwell_time_comparison = float_isclose(self.run_identifier.dwell_time, float(self.ScanParameters["DwellTime"]))
        number_frame_comparison = self.run_identifier.number_frames == int(self.ScanParameters["FramesRequested"])
        image_width_comparison = self.run_identifier.width == int(self.ScanParameters["Image"]["Width"])
        image_height_comparison = self.run_identifier.height == int(self.ScanParameters["Image"]["Height"])

        return all((dwell_time_comparison, number_frame_comparison, image_width_comparison, image_height_comparison))


class StartupProfilerData(ProfilerData):
    @property
    def valid(self) -> bool:
        """Performance validation of the Startup. Verifies if the total time of the Startup exists.

        Returns
        -------
        If the startup time is valid then return True else False
        """
        try:
            test.log("Checking validity valid if Total Time item has been found")
            test.log(f"Total Time : {self.TotalTime}")
        except Exception as ex:
            test.warning(f"Exception of type [{ex.__class__.__name__}] triggered. Arguments [{ex.args}]")
            return False
        return True


class EelsSIProfilerData(ProfilerData):
    @property
    def valid(self) -> bool:
        """Temporary valid method until the profiler data is fixed for EELS SI acquisitions.

        Returns
        -------
        If the startup time is valid then return True else False
        """
        return True


def get_log_file_name_path() -> str:
    """Checks if the velox log file exists with the standard name and returns the log path.

    Returns
    -------
    Returns the path to the log file
    """
    file_utils = FileUtils()

    log_file_dir = os.path.join(file_utils.connection.getEnvironmentVariable("LOCALAPPDATA"), "FEI", "Velox", "Log")

    log_file_log_format_name = "Velox_Dbg.log"
    log_file_txtlog_format_name = "Velox_Dbg.txtlog"

    log_file_log_format_path = os.path.join(log_file_dir, log_file_log_format_name)
    log_file_txtlog_format_path = os.path.join(log_file_dir, log_file_txtlog_format_name)

    log_file_log_format_exists = file_utils.file_exists(log_file_log_format_path)
    log_file_txtlog_format_exists = file_utils.file_exists(log_file_txtlog_format_path)

    if log_file_log_format_exists and log_file_txtlog_format_exists:
        log_file_log_format_modification_datetime = file_utils.get_modification_date(log_file_log_format_path)
        log_file_txtlog_format_modification_datetime = file_utils.get_modification_date(log_file_txtlog_format_path)

        if log_file_log_format_modification_datetime > log_file_txtlog_format_modification_datetime:
            return log_file_log_format_path
        else:
            return log_file_txtlog_format_path

    elif log_file_log_format_exists:
        return log_file_log_format_path

    elif log_file_txtlog_format_exists:
        return log_file_txtlog_format_path

    else:
        raise FileNotFoundError(
            f"Couldn't find `{log_file_log_format_name}` or `{log_file_txtlog_format_name}` in `{log_file_dir}`."
        )


def _find_data(
    profiler_type_tag: PerformanceProfilerType,
    run_identifier: Union[PerformanceRunIdentifier, StemPerformanceRunIdentifier, CameraPerformanceRunIdentifier],
    log_filepath: str,
) -> Union[
    StemSeriesProfilerData, StemProfilerData, SiProfilerData, CameraProfilerData, StartupProfilerData, ProfilerData
]:
    """Reads the velox log file starting at the end until a profiler tag is found from which a ProfilerData type class
    is created and returned from the data in the file.

    Parameters
    ----------
    profiler_type_tag: Determines which profiler tag is being searched on the logfile
    run_identifier: Contains expected data for the performance test and helps determine if a profiler data object
        needs to be created without log file data
    log_filepath: Path to the log file

    Returns
    -------
    Creates and returns a ProfilerData type object
    """
    profile_tag = profiler_type_tag.associated_tag()
    for qline in readline_reverse(log_filepath):
        fnd_index = qline.find(profile_tag)
        if fnd_index != -1:
            test.log(f"Found [{profile_tag}] in [{qline}]")
            str_pos = fnd_index + len(profile_tag)
            qline = qline[str_pos:]
            test.log(qline)
            if profiler_type_tag == PerformanceProfilerType.STEM:
                if run_identifier.number_frames > 1:
                    return StemSeriesProfilerData(run_identifier, qline)
                else:
                    return StemProfilerData(run_identifier, qline)
            elif profiler_type_tag == PerformanceProfilerType.SI:
                return SiProfilerData(run_identifier, qline)
            elif profiler_type_tag == PerformanceProfilerType.CAMERA:
                return CameraProfilerData(run_identifier, qline)
            elif profiler_type_tag == PerformanceProfilerType.STARTUP:
                return StartupProfilerData(run_identifier, qline)
            elif profiler_type_tag == PerformanceProfilerType.EELS:
                return EelsSIProfilerData(run_identifier, qline)

    test.warning(
        f"Not yet able to find a valid profile line for tag {profile_tag}. Returning base-class " f"ProfilerData."
    )
    return ProfilerData(run_identifier)


def get_last_performance_profile_data(
    profiler_tag: PerformanceProfilerType, run_identifier: PerformanceRunIdentifier, log_filepath: str
) -> Union[
    StemSeriesProfilerData, StemProfilerData, SiProfilerData, CameraProfilerData, StartupProfilerData, ProfilerData
]:
    """Get the last performance data for the given profiler data type.

    Parameters
    ----------
    profiler_tag: Determines which profiler tag is being searched on the logfile
    run_identifier: Contains expected data for the performance test and helps determine if a profiler data object
        needs to be created without log file data
    log_filepath: Path to the log file

    Returns
    -------
    Returns a ProfilerData type object
    """
    number_tries = 10
    profile_data = _find_data(profiler_tag, run_identifier, log_filepath)
    while number_tries > 0 and not run_identifier.aborted and not profile_data.valid:
        profile_data = _find_data(profiler_tag, run_identifier, log_filepath)
        number_tries -= 1
        squish.snooze(3)
        test.log("Developer log to be filled with the profiler data")
    if number_tries == 0:
        test.warning("Create Profile Data: Number of tries reached 0")
        run_identifier.aborted = True
    return profile_data
