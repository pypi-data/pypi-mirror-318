"""
A package for calculating the check digit of a KiwiRail TMS number
"""

__version__ = "1.0.0"

from .tms_checkdigit import (
    convert_char_to_digits,
    calculate_check_digit,
)
