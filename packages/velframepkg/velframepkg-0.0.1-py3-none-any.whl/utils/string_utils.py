# Copyright(c) 2021-2023 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import datetime

from quantiphy import Quantity


def remove_suffix(filename: str, suffix: str) -> str:
    if filename.endswith(suffix):
        return filename[: -len(suffix)]
    return filename


def convert_si_unit_to_float(value: str) -> float:
    """Converts a SI string with nm, µm, mm, ns, µs, ms, s to the actual float value.

    Parameters
    ----------
    value: String containing the value

    Returns
    -------
    A float version of the string
    """
    stripped_value = value.strip()
    converted_result = Quantity(stripped_value).real
    return converted_result


def remove_chars(value: str, delete_chars: str, replace_char: str = "_") -> str:
    """Removes a list of specified characters from a string.

    Parameters
    ----------
    value: String were the characters should be removed from
    delete_chars: String with all the characters to check for
    replace_char: Value that will replace the delete_chars value

    Returns
    -------
    The string without the characters in the delete_char parameter.
    """
    for c in delete_chars:
        value = value.replace(c, replace_char)
    return value


def date_as_str() -> str:
    """Returns a timestamp of the current date with the format: YYYY-MM-DD (example: 2015-04-16).

    Returns
    -------
    Current timestamp
    """
    return "%s" % datetime.datetime.now().strftime("%Y-%m-%d")
