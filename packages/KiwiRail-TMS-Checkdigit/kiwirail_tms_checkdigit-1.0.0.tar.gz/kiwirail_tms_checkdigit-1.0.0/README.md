# KiwiRail TMS Checkdigit

A Python package for calculating the check digit of a KiwiRail TMS number.

## Introduction

This package provides a simple way to calculate the check digit of a KiwiRail TMS number. It uses a weighted sum algorithm to calculate the check digit.

## Installation

To install the package, run the following command:

```bash
pip install .
```

## Usage

To use the package, import the `tms_checkdigit` module and call the `calculate_check_digit` function:

```python
from KiwiRail_TMS_Checkdigit import tms_checkdigit

tms_number = "AMA100"
check_digit = tms_checkdigit.calculate_check_digit(tms_number)
print(check_digit)
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
