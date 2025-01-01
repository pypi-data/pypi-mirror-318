# KiwiRail TMS Checkdigit

A Python package for calculating the check digit of a KiwiRail TMS number.

## Introduction

A TMS (Traffic Monitoring System) number is a unique identifier used by KiwiRail to track and manage their locomotives and rolling stock. The TMS number is a combination of letters and numbers, with the last digit being a check digit that is calculated using a weighted sum algorithm. This package provides a simple way to calculate the check digit of a KiwiRail TMS number.

## What is a TMS Number?

A TMS number is a four-digit number that starts with a letter or letters, followed by a series of numbers. The last digit of the TMS number is a check digit that is calculated based on the preceding digits. The TMS number system was introduced in 1979 as part of the computerised Traffic Monitoring System. The system assigns unique numbers to each locomotive and piece of rolling stock, allowing for efficient tracking and management.

For example, the TMS number "DX5016" breaks down as follows:

* "DX" is the class identifier
* "50" is the base number
* "1" is the check digit

The check digit is calculated using a weighted sum algorithm, which ensures that the TMS number is unique and can be verified for accuracy.

## Installation

To install the package, run the following command:

```bash
pip install KiwiRail-TMS-Checkdigit
```

## Usage

To use the package, import the `tms_checkdigit` module and call the `calculate_check_digit` function:

```python
import KiwiRail_TMS_Checkdigit as tms

print(tms.calculate_check_digit("AMA100"))
print(tms.calculate_check_digit("AMA100"))

```

## Testing

To run the tests, use the following command:

```bash
python setup.py test
```

## Contributing

Contributions are welcome! Please submit a pull request with your changes.

## License

This package is licensed under the [MIT License](LICENSE).
