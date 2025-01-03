# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import datetime
import math
import re
import squish
import subprocess
import test
import time
from operator import eq, gt, le, lt, ne
from typing import Callable

from utils.labels.test_utilities import WINDBG_PATH
from velox.labels.acquisition_toolbar import ImagingActions
from velox.labels.acquisition_types import AcquisitionType
from velox.labels.imaging import SeriesModes
from velox.labels.stem_imaging import StemPreset
from velox.labels.time_constants import TimeOut
from velox.labels.toolbar import PresetIndex


def get_scan_acquisition_timeout(
    context, index: PresetIndex, frame_number: int, acquisition_type: AcquisitionType
) -> int:
    """Compute the expected acquisition time according to last set settings, and add a 3 seconds delay.

    Parameters
    ----------
    context: used to retrieve previously set settings
    index: used to identify the preset with the previously set settings
    frame_number: minimum number of frame that should be acquire, used for live view

    Return
    ----------
    scan_duration: expected acquisition duration in seconds (at least 5 seconds, default value is 15)
    """
    default_scan_duration_timeout = TimeOut.DEFAULT_SCAN_DURATION_TIMEOUT
    default_time_offset = TimeOut.ACQUISITION_TIME_OFFSET
    minimum_scan_duration_timeout = TimeOut.MINIMUM_SCAN_DURATION_TIMEOUT
    scan_preset = context.userData[acquisition_type.value].get(index.value)
    image_width = scan_preset.get("image_width")
    image_height = scan_preset.get("image_height")
    dwell_time = scan_preset.get("dwell_time")
    dwell_time_unit = scan_preset.get("dwell_time_unit")
    mode = scan_preset.get("mode")

    if image_width and image_height and dwell_time and dwell_time_unit:
        assert dwell_time_unit in ["us", "µs", "ms", "ns"]
        # compute the duration in ms
        if dwell_time_unit == "us" or dwell_time_unit == "µs":
            scan_duration = image_width * image_height * dwell_time / 1000
        elif dwell_time_unit == "ms":
            scan_duration = image_width * image_height * dwell_time
        elif dwell_time_unit == "ns":
            scan_duration = image_width * image_height * dwell_time / 1000000
        # compute the duration in seconds
        scan_duration = scan_duration / 1000

        if frame_number:
            scan_duration = scan_duration * frame_number
        elif mode == StemPreset.SERIES and scan_preset.get("series_mode") == SeriesModes.AUTO_STOP:
            series_size = int(scan_preset.get("series_size").split(" ")[0])
            scan_duration = scan_duration * series_size
        # compute the duration of the scan plus 3 second
        scan_duration = scan_duration + default_time_offset
    else:
        # default value
        scan_duration = default_scan_duration_timeout

    test.log(
        f"max(minimum_scan_duration, int(scan_duration)) : {max(minimum_scan_duration_timeout, int(scan_duration))}"
    )
    return max(minimum_scan_duration_timeout, int(scan_duration))


class TestUtilities:
    """Provides some test helper functions."""

    @staticmethod
    def wait_for_with_new_attempt_wait(test_function, new_attempt_wait_time, timeout=10):
        """Waits until the specified condition is validated, or the timeout is reached.

        Parameters
        ----------
        test_function: Callable test function returning True or False
        new_attempt_wait_time: Time to wait before a new attempt (Unit : second)
        timeout: Maximum time to wait before considering the test as failed (Unit : second)
                 To disable the timeout, set it to None
        """

        # The function parameter is not a function
        if not callable(test_function):
            return False

        timeout_start = time.time()

        # The function is executed cyclically until the condition is validated, or the timeout occurs
        while not test_function():
            squish.snooze(new_attempt_wait_time)

            if timeout is not None and time.time() >= timeout_start + timeout:
                return False

        return True

    @staticmethod
    def get_tem_acquisition_timeout(context, index: PresetIndex, frame_number: int = None) -> int:
        """Compute the expected acquisition time according to last set tem settings, and add a 3 seconds delay.

        Parameters
        ----------
        context: used to retrieve previously set settings
        index: used to identify the preset with the previously set settings
        frame_number: minimum number of frame that should be acquire, used for live view

        Return
        ----------
        scan_duration : expected acquisition duration in seconds (at least 5 seconds, default value is 15)
        """
        default_scan_duration_timeout = TimeOut.DEFAULT_SCAN_DURATION_TIMEOUT
        default_time_offset = TimeOut.ACQUISITION_TIME_OFFSET
        minimum_scan_duration_timeout = TimeOut.MINIMUM_SCAN_DURATION_TIMEOUT
        tem_preset = context.userData.get(AcquisitionType.TEM.value).get(index.value)
        dwell_time = tem_preset.get("dwell_time")
        dwell_time_unit = tem_preset.get("dwell_time_unit")
        mode = tem_preset.get("mode")

        if dwell_time and dwell_time_unit:
            assert dwell_time_unit in ["us", "µs", "ms", "ns", "s"]
            # compute the duration in ms
            if dwell_time_unit == "us" or dwell_time_unit == "µs":
                scan_duration = dwell_time / 1000
            elif dwell_time_unit == "ms":
                scan_duration = dwell_time * 10
            elif dwell_time_unit == "ns":
                scan_duration = dwell_time / 1000000
            else:
                scan_duration = dwell_time * 10000
            # compute the duration in seconds
            scan_duration = scan_duration / 1000
            if frame_number:
                scan_duration = scan_duration * frame_number
            elif mode == ImagingActions.SERIES and tem_preset.get("series_mode") == SeriesModes.AUTO_STOP:
                series_size = int(tem_preset.get("series_size").split(" ")[0])
                scan_duration = scan_duration * series_size

            # compute the duration of the scan plus 3 second
            scan_duration += default_time_offset
        else:
            # default value
            scan_duration = default_scan_duration_timeout

        return max(minimum_scan_duration_timeout, int(scan_duration))

    @staticmethod
    def get_stem_acquisition_timeout(context, index: PresetIndex, frame_number: int = None) -> int:
        """Compute the expected acquisition time according to last set settings, and add a 3 seconds delay.

        Parameters
        ----------
        context: used to retrieve previously set settings
        index: used to identify the preset with the previously set settings
        frame_number: minimum number of frame that should be acquire, used for live view

        Return
        ----------
        scan_duration : expected acquisition duration in seconds
        """
        return get_scan_acquisition_timeout(context, index, frame_number, AcquisitionType.STEM)

    @staticmethod
    def get_si_acquisition_timeout(context, index: PresetIndex, frame_number: int = None) -> int:
        """Compute the expected acquisition time according to last set settings.

        Parameters
        ----------
        context: used to retrieve previously set settings
        index: used to identify the preset with the previously set settings
        frame_number: minimum number of frame that should be acquire, used for live view

        Return
        ----------
        scan_duration : expected acquisition duration in seconds
        """
        return get_scan_acquisition_timeout(context, index, frame_number, AcquisitionType.SI)

    @staticmethod
    def get_timeout_from_datetime(expected_datetime: datetime.datetime, additional_timeout: int = 10) -> int:
        """Compute the total seconds time from a datetime object with hours:minutes:seconds format.

        Parameters
        ----------
        expected_datetime: Expected timeout to be calculated in seconds
        additional_timeout: Additional time in seconds to avoid possible timing issue with the timeout

        Return
        ------
        Return the total amount of seconds of the datetime object
        """
        if expected_datetime.hour == 0 and expected_datetime.minute == 0 and expected_datetime.second == 0:
            return additional_timeout
        else:
            hours_in_seconds = expected_datetime.hour * 3600
            minutes_in_seconds = expected_datetime.minute * 60
            return hours_in_seconds + minutes_in_seconds + expected_datetime.second + additional_timeout

    @staticmethod
    def retry_upon_except(update_function: Callable, max_retry=2, new_attempt_wait_time=0.1):
        """Waits for the update to be complete without attribute error exception due to internal object update.

        Parameters
        ----------
        update_function: Callable update function
        max_retry: Maximum number of calls of the update function
        new_attempt_wait_time: Time to wait before a new attempt (Unit : second)
        """

        if not callable(update_function):
            return False

        retry = 0
        while retry <= max_retry:
            try:
                update_function()
                return True
            except Exception as exception:  # noqa: E722
                retry += 1
                test.log(f"Exception caught: {exception}")
                squish.snooze(new_attempt_wait_time)
                # For last try do not catch exception
                if retry == max_retry:
                    update_function()
                    return True
        return False

    @staticmethod
    def __eval_nonfatal(val1, comparison, val2, fail_message):
        current_throw_on_failure = squish.testSettings.throwOnFailure

        squish.testSettings.throwOnFailure = False
        test_value = comparison(val1, val2)

        if not test_value:
            test.fail(fail_message)

        squish.testSettings.throwOnFailure = current_throw_on_failure

        return test_value

    @staticmethod
    def __eval_fatal(val1, comparison, val2, fail_message):
        current_throw_on_failure = squish.testSettings.throwOnFailure

        squish.testSettings.throwOnFailure = True
        test_value = comparison(val1, val2)

        if not test_value:
            test.fatal(fail_message)

        squish.testSettings.throwOnFailure = current_throw_on_failure

        return test_value

    @staticmethod
    def expect_eq(value1, value2, fail_message=""):
        return TestUtilities.__eval_nonfatal(value1, eq, value2, fail_message)

    @staticmethod
    def assert_eq(value1, value2, fail_message=""):
        TestUtilities.__eval_fatal(value1, eq, value2, fail_message)

    @staticmethod
    def assert_ne(value1, value2, fail_message=""):
        TestUtilities.__eval_fatal(value1, ne, value2, fail_message)

    @staticmethod
    def expect_gt(value1, value2, fail_message=""):
        return TestUtilities.__eval_nonfatal(value1, gt, value2, fail_message)

    @staticmethod
    def assert_gt(value1, value2, fail_message=""):
        TestUtilities.__eval_fatal(value1, gt, value2, fail_message)

    @staticmethod
    def expect_lt(value1, value2, fail_message=""):
        TestUtilities.__eval_nonfatal(value1, lt, value2, fail_message)

    @staticmethod
    def assert_lt(value1, value2, fail_message=""):
        TestUtilities.__eval_fatal(value1, lt, value2, fail_message)

    @staticmethod
    def assert_le(value1, value2, fail_message=""):
        TestUtilities.__eval_fatal(value1, le, value2, fail_message)

    @staticmethod
    def assert_closeto(value1, value2, tolerance, fail_message=""):
        """Check that 2 values are close with a certain tolerance value.

        Parameters
        ----------
        value1, value2: values to compare
        tolerance: % of tolerance example for 5% is 0.05
        fail_message: the message this assertation is bound to.
        """
        test.verify(math.isclose(value1, value2, rel_tol=tolerance, abs_tol=0.0), fail_message)

    @staticmethod
    def expect_closeto(value1, value2, tolerance, message=""):
        """Check that 2 values are close with a certain tolerance value.

        Parameters
        ----------
        value1, value2: values to compare
        tolerance: % of tolerance example for 5% is 0.05
        message: the message this verification is bound to.
        """
        test.verify(math.isclose(value1, value2, rel_tol=tolerance, abs_tol=0.0), message)

    @staticmethod
    def expect_in_range(value1, value2, value_range: int, message: str):
        """Check if the two given values is more or less inside the informed range.

        Parameters
        ----------
        value1: first value
        value2: second value
        value_range: range for more or less
        message: something

        Returns
        -------
        true if the difference between value1 and value2 are within range, and false if it is not.
        """
        value = abs(value1 - value2)
        test.verify(value <= value_range, message)

    @staticmethod
    def assert_regex(regex, value, fail_message):
        current_throw_on_failure = squish.testSettings.throwOnFailure

        squish.testSettings.throwOnFailure = True

        assert re.match(regex, value) is not None, fail_message

        squish.testSettings.throwOnFailure = current_throw_on_failure

    @staticmethod
    def attach_image_to_test(img, message):
        test.attachImage(img, message)

    @staticmethod
    def wait_for(check_function: Callable, timeout=5, new_attempt_wait_time=0.1):
        """Waits for the check function to be complete and return True if succeed, else return False if last check after
        timeout is failed.

        Parameters
        ----------
        check_function: Callable update function
        timeout: timeout before last check
        new_attempt_wait_time: Time to wait before a new attempt (Unit : second)
        """

        if not callable(check_function):
            return False

        start_time = time.time()
        end_time = start_time + timeout
        while time.time() <= end_time:
            result = check_function()
            if result:
                return True
            squish.snooze(new_attempt_wait_time)
        result = check_function()
        if result:
            return True
        return False


def windbg_extract_call_stack_to_file(dump_file: str, out_file: str):
    """Extracts the call stack from a dump file using WinDbg and writes it to the given file.

    Parameters
    ----------
    dump_path: path to the dump file to extract call stack from
    out_file: path to the file to write the call stack to
    """
    command = [
        WINDBG_PATH,
        "-c",
        ".ecxr;k;q",
        "-z",
        dump_file,
    ]

    try:
        with open(out_file, "w") as output_file:
            subprocess.run(command, check=True, stdout=output_file)
    except subprocess.CalledProcessError as ex:
        test.warning(f"Error running WinDbg: {repr(ex)}")
