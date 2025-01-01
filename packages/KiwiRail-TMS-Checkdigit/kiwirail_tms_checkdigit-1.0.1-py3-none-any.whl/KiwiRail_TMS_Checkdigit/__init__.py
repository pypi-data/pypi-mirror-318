"""
A package for calculating the check digit of a KiwiRail TMS number
"""

__version__ = "1.0.1"

from .tms_checkdigit import (
    is_check_digit_valid,
    calculate_check_digit,
)
