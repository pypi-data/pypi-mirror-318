# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import datetime
import json
import os
import squish
import test
from dataclasses import dataclass
from typing import Tuple, Union

from common.environment import Environment
from common.file_utils import FileUtils, readline_reverse
from utils.mathematical_tools import float_isclose
from utils.string_utils import convert_si_unit_to_float, date_as_str
from velox.configuration import MicroscopeConfiguration
from velox.labels.performance import ProfilerTypeTag


class RunIdentifier:
    def __init__(
        self,
        step_index: int,
        step_name: str,
        dwell_time: str = "0",
        number_elements: int = 0,
        number_frames: int = 0,
        width: int = 0,
        height: int = 0,
        magnification: int = 0,
        number_detectors: int = 1,
    ):
        self.step_index = step_index
        self.step_name = step_name
        self.dwell_time = convert_si_unit_to_float(dwell_time)
        self.number_elements = number_elements
        self.number_frames = number_frames
        self.width = width
        self.height = height
        self.magnification = magnification
        self.number_detectors = number_detectors
        self.aborted = False

    def __str__(self) -> str:
        return (
            f"Dwell time:[{self.dwell_time}] "
            f"Number of Elements:[{self.number_elements}] "
            f"Number of Frames:[{self.number_frames}] "
            f"W X H:[{self.width}]x[{self.height}] "
            f"Magnification:[{self.magnification}] "
            f"Number of Detectors:[{self.number_detectors}]"
        )


@dataclass
class CameraRunIdentifier:
    step_index: int = None
    step_name: str = None
    exposure_time: str = None
    binning: str = None
    readout_name: str = None
    width: int = None
    height: int = None
    image_size: str = None
    number_of_frames: int = None

    def __post_init__(self):
        if self.exposure_time:
            self.exposure_time = convert_si_unit_to_float(self.exposure_time)
        self.aborted = False


class ProfilerData:
    def __init__(
        self,
        velox_version: str = "",
        run_identifier: Union[RunIdentifier, CameraRunIdentifier] = None,
        json_data: str = None,
        log_time: str = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
    ):
        if json_data is not None:
            self.__dict__ = json.loads(json_data)
        self._microscope_configuration = MicroscopeConfiguration()
        self.log_time = datetime.datetime.strptime(log_time, "%Y-%m-%dT%H:%M:%S.%f")
        self.run_identifier = run_identifier
        self.velox_version = velox_version

    @property
    def valid(self) -> bool:
        """Performance validation but always False because no actual line has been found when a nonspecific Profiler
        Data is used.

        Return
        ------
        Always False because no actual line has been found
        """
        return False

    @property
    def csv_format(self) -> str:
        """Return the settings values in a phrase separated by a semicolon (csv format).

        Return
        ------
        String of csv settings values
        """
        return f"{','.join(self.get_csv_settings())}\n"

    def get_csv_settings(self) -> list:
        """Return the settings of the test environment common between performance tests.

        Return
        ------
        List of csv settings values
        """
        return [
            Environment().get_system_configuration_name(),
            self.velox_version,
            self._microscope_configuration.tem_version_raw,
            date_as_str(),
            f"{self.run_identifier.step_name}.{self.run_identifier.step_index:02d}",
        ]

    @property
    def csv_header(self) -> list:
        """Return the settings header of the test environment common between performance tests.

        Return
        ------
        List of csv settings header
        """
        return ["Machine", "Velox Version", "Server Version", "Date", "Test Step"]


class StemSeriesProfilerData(ProfilerData):
    @property
    def valid(self) -> bool:
        """Performance validation of the STEM Series. Verifies if all STEM Series settings values match the expected
        values defined in the identifier.

        Return
        ------
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

    @property
    def csv_header(self) -> str:
        """Return the STEM Series csv header alongside the environment settings header (in csv format).

        Return
        ------
        String of csv settings header for STEM series
        """
        csv_header_list = ProfilerData.csv_header.fget(self)
        csv_header_list.append("Number detectors")
        csv_header_list.append("Resolution")
        csv_header_list.append("Dwell Time [s]")
        csv_header_list.append("Frames requested")
        csv_header_list.append("Frames acquired")
        csv_header_list.append("Frame time [s]")
        csv_header_list.append("Frames per second")
        csv_header_list.append("Overhead")
        csv_header_string = ",".join(csv_header_list)
        return f"{csv_header_string}\n"

    def get_csv_settings(self) -> list:
        """Return the STEM Series csv settings alongside the environment settings values.

        Return
        ------
        List of csv settings values
        """
        csv_settings_list = super(StemSeriesProfilerData, self).get_csv_settings()
        if not self.run_identifier.aborted:
            percentage = 1.2  # 20% overhead
            number_detectors = self.ScanParameters["NrDetectors"]
            width = self.ScanParameters["Image"]["Width"]
            height = self.ScanParameters["Image"]["Height"]
            dwell_time = self.ScanParameters["DwellTime"]
            frames_acquisition = self.Frames
            frame_time = width * height * dwell_time * percentage
            frames_per_second = frames_acquisition / (
                self.TotalTime - self.OverheadBeforeStart - self.OverheadAfterStop
            )
            overhead = 1 - frames_per_second * frame_time / percentage
            csv_settings_list.append(f"{number_detectors}")
            csv_settings_list.append(f"{width}x{height}")
            csv_settings_list.append(f"{dwell_time}")
            csv_settings_list.append(f"{self.ScanParameters['FramesRequested']}")
            csv_settings_list.append(f"{frames_acquisition}")
            csv_settings_list.append(f"{frame_time}")
            csv_settings_list.append(f"{frames_per_second}")
            csv_settings_list.append(f"{overhead}")
        else:
            csv_settings_list.append(f"{self.run_identifier.number_detectors}")
            csv_settings_list.append(f"{self.run_identifier.width}x{self.run_identifier.height}")
            csv_settings_list.append(f"{self.run_identifier.dwell_time}")
            csv_settings_list.append(f"{self.run_identifier.number_frames}")
            for i in range(4):
                csv_settings_list.append("FAILED")
        return csv_settings_list


class SiProfilerData(ProfilerData):
    @property
    def valid(self) -> bool:
        """Performance validation of the SI (Spectrum Imaging). Verifies if all SI settings values match the expected
        values defined in the identifier.

        Return
        ------
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

    @property
    def csv_header(self) -> str:
        """Return the SI (Spectrum Imaging) csv header alongside the environment settings header (in csv format).

        Return
        ------
        String of csv settings header for SI
        """
        csv_header_list = ProfilerData.csv_header.fget(self)
        csv_header_list.append("Detector Type")
        csv_header_list.append("Selected Area Size")
        csv_header_list.append("Number of Elements")
        csv_header_list.append("Image Height [pixels]")
        csv_header_list.append("Image Width [pixels]")
        csv_header_list.append("Selected Area")
        csv_header_list.append("Dwell Time [s]")
        csv_header_list.append("Total Time [s]")
        csv_header_list.append("Number of frames")
        csv_header_list.append("Total performance [spectra/sec]")
        csv_header_list.append("Performance without start/stop overhead [spectra/sec]")
        csv_header_list.append("Overhead per point [s]")
        csv_header_list.append("Overhead per point without start/stop overhead [s]")
        csv_header_string = ",".join(csv_header_list)
        return f"{csv_header_string}\n"

    def get_csv_settings(self) -> list:
        """Return the SI (Spectrum Imaging) csv settings alongside the environment settings values.

        Return
        ------
        List of csv settings values
        """
        # calculate values
        csv_settings_list = super(SiProfilerData, self).get_csv_settings()
        csv_settings_list.append(self._microscope_configuration.eds_detector_type)
        if not self.run_identifier.aborted:
            frames = self.Frames
            dwell_time = self.ScanParameters["DwellTime"]
            selected_area_width = self.ScanParameters["Image"]["Width"] * (
                self.ScanParameters["SelectedArea"]["Right"] - self.ScanParameters["SelectedArea"]["Left"]
            )
            selected_area_height = self.ScanParameters["Image"]["Height"] * (
                self.ScanParameters["SelectedArea"]["Bottom"] - self.ScanParameters["SelectedArea"]["Top"]
            )
            total_performance = (selected_area_width * selected_area_height * frames) / self.TotalTime
            total_performance_no_overhead = (selected_area_width * selected_area_height * frames) / (
                self.TotalTime - self.OverheadBeforeStart - self.OverheadAfterStop
            )
            overhead_per_point = (1 / total_performance) - dwell_time
            overhead_per_point_no_startstop = (1 / total_performance_no_overhead) - dwell_time
            selected_area = self.ScanParameters["SelectedArea"]["Right"] - self.ScanParameters["SelectedArea"]["Left"]
            # add values
            csv_settings_list.append(f"{selected_area_width}x{selected_area_height}")
            csv_settings_list.append(f"{len(self.SpectrumImagingParameters['SelectedElements'])}")
            csv_settings_list.append(f"{self.ScanParameters['Image']['Width']}")
            csv_settings_list.append(f"{self.ScanParameters['Image']['Height']}")
            csv_settings_list.append(f"{selected_area}")
            csv_settings_list.append(f"{dwell_time}")
            csv_settings_list.append(f"{self.TotalTime}")
            csv_settings_list.append(f"{frames}")
            csv_settings_list.append(f"{total_performance}")
            csv_settings_list.append(f"{total_performance_no_overhead}")
            csv_settings_list.append(f"{overhead_per_point}")
            csv_settings_list.append(f"{overhead_per_point_no_startstop}")
        else:
            csv_settings_list.append(f"{self.run_identifier.width}x{self.run_identifier.height}")
            csv_settings_list.append(f"{self.run_identifier.number_elements}")
            csv_settings_list.append(f"{self.run_identifier.width}")
            csv_settings_list.append(f"{self.run_identifier.height}")
            csv_settings_list.append("1")
            csv_settings_list.append(f"{self.run_identifier.dwell_time}")
            for i in range(6):
                csv_settings_list.append("FAILED")
        return csv_settings_list


class CameraProfilerData(ProfilerData):
    @property
    def csv_header(self) -> str:
        """Return the Camera csv header alongside the environment settings header (in csv format).

        Return
        ------
        String of csv settings header for SI
        """
        csv_header_list = ProfilerData.csv_header.fget(self)
        csv_header_list.append("Camera Type")
        csv_header_list.append("Selected Area")
        csv_header_list.append("Image Size")
        csv_header_list.append("Exposure Time")
        csv_header_list.append("Readout Area")
        csv_header_list.append("Binning")
        csv_header_list.append("Number of Frames")
        csv_header_list.append("Total Time")
        csv_header_list.append("Total performance (fps)")
        csv_header_list.append("Total performance without start/stop overhead (fps)")
        csv_header_string = ",".join(csv_header_list)
        return f"{csv_header_string}\n"

    @property
    def valid(self) -> bool:
        """Performance validation of the Camera. Verifies if all Camera settings values match the expected values
        defined in the identifier.

        Return
        ------
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

    def get_csv_settings(self) -> list:
        """Return the Camera csv settings alongside the environment settings values.

        Return
        ------
        List of csv settings values
        """
        # calculate values
        csv_settings_list = super(CameraProfilerData, self).get_csv_settings()
        csv_settings_list.append(self._microscope_configuration.camera_type)
        if not self.run_identifier.aborted:
            # read values and calculate the performance
            total_time = self.TotalTime
            overhead_before_start = self.OverheadBeforeStart
            overhead_after_stop = self.OverheadAfterStop
            frames = self.Frames
            width = int(self.CameraParameters["ReadOutArea"]["Right"]) - int(
                self.CameraParameters["ReadOutArea"]["Left"]
            )
            height = int(self.CameraParameters["ReadOutArea"]["Bottom"]) - int(
                self.CameraParameters["ReadOutArea"]["Top"]
            )
            exposure_time = self.CameraParameters["ExposureTime"]
            readout_name = self.run_identifier.readout_name
            binning = self.CameraParameters["Binning"]["X"]
            image_size = self.run_identifier.image_size
            total_performance = max(frames - 1, 0) / self.TotalTime
            total_performance_no_overhead = max(frames - 1, 0) / (
                self.TotalTime - overhead_before_start - overhead_after_stop
            )
            # add values
            csv_settings_list.append(f"{width}x{height}")
            csv_settings_list.append(f"{image_size}x{image_size}")
            csv_settings_list.append(f"{exposure_time}")
            csv_settings_list.append(f"{readout_name}")
            csv_settings_list.append(f"{binning}")
            csv_settings_list.append(f"{frames}")
            csv_settings_list.append(f"{total_time}")
            csv_settings_list.append(f"{total_performance}")
            csv_settings_list.append(f"{total_performance_no_overhead}")
        else:
            csv_settings_list.append(f"{self.run_identifier.width}x{self.run_identifier.height}")
            csv_settings_list.append(f"{self.run_identifier.image_size}x{self.run_identifier.image_size}")
            csv_settings_list.append(f"{self.run_identifier.exposure_time}")
            csv_settings_list.append(f"{self.run_identifier.readout_name}")
            csv_settings_list.append(f"{self.run_identifier.binning}")
            for i in range(4):
                csv_settings_list.append("FAILED")
        return csv_settings_list


class StemProfilerData(ProfilerData):
    @property
    def valid(self) -> bool:
        """Performance validation of the STEM. Verifies if all STEM settings values match the expected values defined in
        the identifier.

        Return
        ------
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

    @property
    def csv_header(self) -> str:
        """Return the STEM csv header alongside the environment settings header (in csv format).

        Return
        ------
        String of csv settings header for SI
        """
        csv_header_list = ProfilerData.csv_header.fget(self)
        csv_header_list.append("Magnification")
        csv_header_list.append("Resolution")
        csv_header_list.append("Dwell Time [s]")
        csv_header_list.append("FT [s]")
        csv_header_list.append("LT [ms]")
        csv_header_list.append("Performance [frame/s]")
        csv_header_list.append("OH [%]")
        csv_header_list.append("Total start/stop time")
        csv_header_string = ",".join(csv_header_list)
        return f"{csv_header_string}\n"

    def get_csv_settings(self) -> list:
        """Return the STEM csv settings alongside the environment settings values.

        Return
        ------
        List of csv settings values
        """
        csv_settings_list = super(StemProfilerData, self).get_csv_settings()
        if not self.run_identifier.aborted:
            # calculate values
            percentage = float(1.2)  # 20 percent overhead
            dwell_time = self.ScanParameters["DwellTime"]
            selected_area_width = self.ScanParameters["Image"]["Width"] * (
                self.ScanParameters["SelectedArea"]["Right"] - self.ScanParameters["SelectedArea"]["Left"]
            )
            selected_area_height = self.ScanParameters["Image"]["Height"] * (
                self.ScanParameters["SelectedArea"]["Bottom"] - self.ScanParameters["SelectedArea"]["Top"]
            )
            ft = (selected_area_width * selected_area_height) * dwell_time * percentage
            lt = 1000 * ft / selected_area_height
            total_start_stop_overhead = self.OverheadBeforeStart + self.OverheadAfterStop
            frame_per_second = self.Frames / (self.TotalTime - total_start_stop_overhead)
            oh = 1 - frame_per_second * ft / percentage
            # add values
            csv_settings_list.append(f"{self.run_identifier.magnification}")
            csv_settings_list.append(f"{selected_area_width}x{selected_area_height}d")
            csv_settings_list.append(f"{dwell_time}")
            csv_settings_list.append(f"{ft}")
            csv_settings_list.append(f"{lt}")
            csv_settings_list.append(f"{frame_per_second}")
            csv_settings_list.append(f"{oh:.2f}")
            csv_settings_list.append(f"{total_start_stop_overhead}")
        else:
            csv_settings_list.append(f"{self.run_identifier.magnification}")
            csv_settings_list.append(f"{self.run_identifier.width}x{self.run_identifier.height}")
            csv_settings_list.append(f"{self.run_identifier.dwell_time}")
            for i in range(5):
                csv_settings_list.append("FAILED")
        return csv_settings_list


class StartupProfilerData(ProfilerData):
    @property
    def csv_header(self) -> str:
        """Return the Startup csv header alongside the environment settings header (in csv format).

        Return
        ------
        String of csv settings header for SI
        """
        csv_header_list = ProfilerData.csv_header.fget(self)
        csv_header_list.append("Total Time (sec)")
        csv_header_string = ",".join(csv_header_list)
        return f"{csv_header_string}\n"

    def get_csv_settings(self) -> list:
        """Return the Startup csv settings alongside the environment settings values.

        Return
        ------
        List of csv settings values
        """
        csv_settings_list = super(StartupProfilerData, self).get_csv_settings()
        if not self.run_identifier.aborted:
            csv_settings_list.append(str(self.TotalTime))
        else:
            csv_settings_list.append("FAILED")
        return csv_settings_list

    @property
    def valid(self) -> bool:
        """Performance validation of the Startup. Verifies if the total time of the Startup exists.

        Return
        ------
        If the startup time is valid then return True else False
        """
        try:
            test.log("Checking validity valid if Total Time item has been found")
            test.log(f"Total Time : {self.TotalTime}")
        except Exception as ex:
            test.warning(f"Exception of type [{ex.__class__.__name__}] triggered. Arguments [{ex.args}]")
            return False
        return True


class VeloxLogReader:
    def __init__(self, velox_version: str):
        self.velox_version = velox_version
        self._log_filepath, self._log_filename = self._get_log_file_name_path()

    def _get_log_file_name_path(self) -> Tuple[str, str]:
        """Checks if the velox log file exists with the standard name and returns the log path and name.

        Return
        ------
        Returns the path to the log file and also the log file name separate
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
                return log_file_log_format_path, log_file_log_format_name
            else:
                return log_file_txtlog_format_path, log_file_txtlog_format_name

        elif log_file_log_format_exists:
            return log_file_log_format_path, log_file_log_format_name

        elif log_file_txtlog_format_exists:
            return log_file_txtlog_format_path, log_file_txtlog_format_name

        else:
            raise FileNotFoundError(
                f"Couldn't find `{log_file_log_format_name}` or `{log_file_txtlog_format_name}` in `{log_file_dir}`."
            )

    def _find_data(
        self, profiler_tag: ProfilerTypeTag, run_identifier: RunIdentifier
    ) -> Union[
        StemSeriesProfilerData, StemProfilerData, SiProfilerData, CameraProfilerData, StartupProfilerData, ProfilerData
    ]:
        """Reads the velox log file starting at the end until a profiler tag is found from which a ProfilerData type
        class is created and returned from the data in the file.

        Parameters
        ----------
        profiler_tag: Determines which profiler tag is being searched on the logfile
        run_identifier: Contains expected data for the performance test and helps determine if a profiler data object
            needs to be created without log file data

        Return
        ------
        Creates and returns a ProfilerData type object
        """
        if run_identifier.aborted:
            if profiler_tag == ProfilerTypeTag.STEM:
                if run_identifier.number_frames > 1:
                    return StemSeriesProfilerData(self.velox_version, run_identifier)
                else:
                    return StemProfilerData(self.velox_version, run_identifier)
            elif profiler_tag == ProfilerTypeTag.SI:
                return SiProfilerData(self.velox_version, run_identifier)
            elif profiler_tag == ProfilerTypeTag.CAMERA:
                return CameraProfilerData(self.velox_version, run_identifier)
            elif profiler_tag == ProfilerTypeTag.STARTUP:
                return StartupProfilerData(self.velox_version, run_identifier)
        for qline in readline_reverse(self._log_filepath):
            fnd_index = qline.find(profiler_tag.value)
            if fnd_index != -1:
                test.log(f"Found [{profiler_tag.value}] in [{qline}]")
                log_time = qline[0 : qline.find("[") - 1]
                str_pos = fnd_index + len(profiler_tag.value)
                qline = qline[str_pos:]
                test.log(qline)
                if profiler_tag == ProfilerTypeTag.STEM:
                    if run_identifier.number_frames > 1:
                        return StemSeriesProfilerData(self.velox_version, run_identifier, qline, log_time)
                    else:
                        return StemProfilerData(self.velox_version, run_identifier, qline, log_time)
                elif profiler_tag == ProfilerTypeTag.SI:
                    return SiProfilerData(self.velox_version, run_identifier, qline, log_time)
                elif profiler_tag == ProfilerTypeTag.CAMERA:
                    return CameraProfilerData(self.velox_version, run_identifier, qline, log_time)
                elif profiler_tag == ProfilerTypeTag.STARTUP:
                    return StartupProfilerData(self.velox_version, run_identifier, qline, log_time)
        test.warning(
            f"Not yet able to find a valid profile line for tag {profiler_tag.value}. Returning base-class "
            f"ProfilerData."
        )
        return ProfilerData(self.velox_version, run_identifier)

    def _in_range(
        self,
        current_time: datetime,
        profile_data: Union[
            StemProfilerData, StemSeriesProfilerData, SiProfilerData, CameraProfilerData, StartupProfilerData
        ],
        number_range: int = 30,
    ) -> bool:
        """Checks if the profile data log time is in a given range of the current time.

        Parameters
        ----------
        current_time: Datetime object with the current timestamp before calling this function
        profile_data: ProfilerData type object containing log timestamp
        number_range: Value of the range which the log timestamp should be in from current time

        Return
        ------
        True if log time is in range else False.
        """
        min_before = False
        min_after = False
        if profile_data is not None:
            min_before = (current_time - profile_data.log_time).seconds < number_range
            min_after = (profile_data.log_time - current_time).seconds < number_range
            test.log(f"min_before: {(current_time - profile_data.log_time).seconds}")
            test.log(f"min_after: {(profile_data.log_time - current_time).seconds}")
            test.log(f"Current time: {current_time.hour}:{current_time.minute}:{current_time.second}")
            test.log(
                f"Profile time: {profile_data.log_time.hour}:{profile_data.log_time.minute}:"
                f"{profile_data.log_time.second}"
            )
            test.log(f"Time range check: result is {min_after or min_before}")
        else:
            test.warning("Time range check: profile_data not found")
        return min_after or min_before

    def _create_profiler_data(
        self, profiler_tag: ProfilerTypeTag, run_identifier: RunIdentifier
    ) -> Union[
        StemSeriesProfilerData, StemProfilerData, SiProfilerData, CameraProfilerData, StartupProfilerData, ProfilerData
    ]:
        """Waits for the log file to be ready and then create and return the ProfileData type object.

        Parameters
        ----------
        profiler_tag: Determines which profiler tag is being searched on the logfile
        run_identifier: Contains expected data for the performance test and helps determine if a profiler data object
            needs to be created without log file data

        Return
        ------
        Returns a ProfilerData type object
        """
        current_time = datetime.datetime.now()
        number_tries = 10
        profile_data = self._find_data(profiler_tag, run_identifier)
        # Log-item should be within 30 seconds of the current time and created with same settings as run identifier
        # But, due to the microscope system time not being synchronized with its timezone there is now a few minutes of
        # difference so the time range has been increased to 10 minutes
        while (
            number_tries > 0
            and not run_identifier.aborted
            and (not profile_data.valid or not self._in_range(current_time, profile_data, 600))
        ):
            current_time = datetime.datetime.now()
            profile_data = self._find_data(profiler_tag, run_identifier)
            number_tries -= 1
            squish.snooze(3)
            test.log("Developer log to be filled with the profiler data")
        if number_tries == 0:
            test.warning("Create Profile Data: Number of tries reached 0")
            run_identifier.aborted = True
        return profile_data

    def get_last_perf_data(
        self, profiler_tag: ProfilerTypeTag, run_identifier: RunIdentifier
    ) -> Union[
        StemSeriesProfilerData, StemProfilerData, SiProfilerData, CameraProfilerData, StartupProfilerData, ProfilerData
    ]:
        """Get the last performance data for the given profiler data type.

        Parameters
        ----------
        profiler_tag: Determines which profiler tag is being searched on the logfile
        run_identifier: Contains expected data for the performance test and helps determine if a profiler data object
            needs to be created without log file data

        Return
        ------
        Returns a ProfilerData type object
        """
        return self._create_profiler_data(profiler_tag, run_identifier)
