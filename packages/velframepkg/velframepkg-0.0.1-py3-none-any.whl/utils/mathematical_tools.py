# Copyright(c) 2021-2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
from decimal import ROUND_HALF_DOWN, ROUND_HALF_UP, Decimal

from common.labels.widgets_states import ComparisonType


class MathematicalTools:
    """Provides some mathematical helper functions."""

    @staticmethod
    def change_angle_interval(value, interval_min, interval_max):
        """Converts the specified angle into the specified interval.

        Parameters
        ----------
        value: Angle to convert
        interval_min: The lower limit of the interval angle.
        interval_max: The upper limit of the interval angle.

        Returns
        -------
        the converted angle in the specified interval
        """

        filtered_value = value

        while filtered_value < interval_min or filtered_value >= interval_max:
            if filtered_value < interval_min:
                filtered_value = interval_max - abs(interval_min - filtered_value)
            elif filtered_value >= interval_max:
                filtered_value = interval_min + abs(filtered_value - interval_max)

        return filtered_value

    @staticmethod
    def round_half_up(x: float, precision: float) -> float:
        """Round using the half up method.

        Parameters
        ----------
        x: float to round
        precision: expected precision, one of 0.1, 0.01, etc.

        Returns
        -------
        the rounded float value
        """

        return float(Decimal(str(x)).quantize(Decimal(str(1 + precision)), rounding=ROUND_HALF_UP))

    @staticmethod
    def round_half_down(x: float, precision: float) -> float:
        """Round using the half down method.

        Parameters
        ----------
        x: float to round
        precision: expected precision, one of 0.1, 0.01, etc.

        Returns
        -------
        the rounded float value
        """

        return float(Decimal(str(x)).quantize(Decimal(str(1 + precision)), rounding=ROUND_HALF_DOWN))

    @staticmethod
    def compare_display_values(comparison_type: ComparisonType, value1: float, value2: float):
        """This function compares two values on the display.

        Parameters
        ----------
        comparison_type: the type of change in between the display values
        value1: First value to compare
        value2: Second value to compare
        """
        if comparison_type == ComparisonType.LARGER:
            variation = value1 > value2
            return variation
        elif comparison_type == ComparisonType.SMALLER:
            variation = value1 < value2
            return variation
        elif comparison_type == ComparisonType.EQUAL:
            variation = value1 == value2
            return variation


def float_isclose(a: float, b: float, rel_tol: float = 1e-09, abs_tol: float = 0.0) -> bool:
    """Returns True if "a" is close in value to "b". False otherwise.

    Parameters
    ----------
    a: one of the values to be tested
    b: the other value to be tested
    rel_tol: The relative tolerance -- the amount of error
                            allowed, relative to the magnitude of the input
                            values.
    abs_tol: The minimum absolute tolerance level -- useful for
                           comparisons to zero.

    Returns
    -------
    True if "a" is close in value to "b". False otherwise
    """
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
