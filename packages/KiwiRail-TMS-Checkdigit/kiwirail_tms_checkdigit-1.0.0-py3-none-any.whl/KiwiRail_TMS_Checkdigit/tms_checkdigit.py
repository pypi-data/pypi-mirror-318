def convert_char_to_digits(char: str) -> list[int]:
    """
    Converts a character to a list of digits based on its ASCII value.

    This function takes a single character as input and returns a list of digits.
    The conversion is done by subtracting 64 from the ASCII value of the character,
    which gives a value between 1 and 26 for letters. The result is then zero-padded
    to two digits.

    For example, the letter "A" has an ASCII value of 65, so it is converted to:
    65 -> 1 -> 01 -> [0, 1]

    Args:
        char (str): The character to convert.

    Returns:
        list[int]: A list of digits representing the character.
    """

    if char.isalpha():
        # Convert the letter to its corresponding numerical value (A=1, B=2, ..., Z=26)
        ascii_value = ord(char.upper()) - 64
        # Return a list with two digits: the tens digit and the ones digit
        return [ascii_value // 10, ascii_value % 10]

    elif char.isdigit():
        # If the character is a digit, simply convert it to an integer and return it as a list
        return [int(char)]

    else:
        # If the character is neither a letter nor a digit, raise a ValueError
        raise ValueError(
            f"Invalid character {char}, only Letters or Numbers are allowed!"
        )


def raw_check_digit_calculation(tms_number: str) -> int:
    """
    Calculates the raw check digit for a given TMS number.

    This function takes a TMS number as input, pads it with zeros to make it 6 characters long,
    and then calculates the weighted sum of the digits in the padded TMS number.
    The weighted sum is then used to calculate the check digit.

    The calculation is done as follows:
    1. Pad the TMS number with zeros to make it 6 characters long.
    2. Convert each character in the padded TMS number to digits using the convert_char_to_digits function.
    3. Calculate the weighted sum of the digits by multiplying each digit by 2 raised to the power of its index.
    4. Calculate the check digit by taking the remainder of the weighted sum when divided by 11.

    Args:
        tms_number (str): The TMS number to calculate the check digit for.

    Returns:
        int: The calculated check digit.
    """
    # Count the number of leading letters in the TMS number
    leading_letters = next(
        (i for i, char in enumerate(tms_number) if not char.isalpha()), len(tms_number)
    )

    # Pad the TMS number with zeros to make it 6 characters long
    # For example, "DSA48" becomes "DSA048" and "RM3" becomes "RM0003"
    padded_tms_number = tms_number[:leading_letters] + tms_number[
        leading_letters:
    ].zfill(6 - leading_letters)

    # Initialize the weighted sum
    weighted_sum = 0
    digit_index = 0

    # Convert each character in the padded TMS number to digits and calculate the weighted sum
    for char in padded_tms_number:
        for digit in convert_char_to_digits(char):
            # Calculate the weighted sum by multiplying each digit by 2 raised to the power of its index
            weighted_sum += digit * (2**digit_index)
            digit_index += 1

    # Calculate the check digit by taking the remainder of the weighted sum when divided by 11
    return weighted_sum % 11


def tms_number_format_valid(tms_number: str, length: int = 6) -> bool:
    """
    Checks if a given TMS number is in a valid format.

    A TMS number is valid if it meets the following conditions:
    - It is not empty
    - It is not longer than the specified length
    - It starts with a letter
    - It ends with a digit
    - It only contains alphanumeric characters

    Args:
        tms_number (str): The TMS number to check.
        length (int): The maximum allowed length of the TMS number. Defaults to 6.

    Returns:
        bool: True if the TMS number is valid, False otherwise.
    """
    return (
        len(tms_number) > 0
        and len(tms_number) <= length
        and tms_number[0].isalpha()
        and tms_number[-1].isdigit()
        and tms_number.isalnum()
    )


def calculate_check_digit(tms_number: str) -> int:
    """
    Calculates the check digit for a given TMS number.

    This function first checks if the input TMS number is valid using the tms_number_format_valid function.
    If the TMS number is valid, it calculates the check digit using the raw_check_digit_calculation function.

    Args:
        tms_number (str): The TMS number to calculate the check digit for.

    Returns:
        int: The calculated check digit.

    Raises:
        ValueError: If the input TMS number is not valid.
    """
    # Validate the input TMS number
    if not tms_number_format_valid(tms_number):
        raise ValueError("Invalid TMS number")

    return raw_check_digit_calculation(tms_number)


def is_check_digit_valid(tms_number: str) -> bool:
    """
    Checks if the check digit of a given TMS number is valid.

    This function first checks if the input TMS number is valid using the tms_number_format_valid function.
    If the TMS number is valid, it calculates the check digit using the raw_check_digit_calculation function
    and compares it to the last digit of the TMS number.

    Args:
        tms_number (str): The TMS number to check.

    Returns:
        bool: True if the check digit is valid, False otherwise.
    """
    # Validate the input TMS number
    if not tms_number_format_valid(tms_number, 7):
        return False

    # Calculate the check digit for the given TMS number
    calculated_check_digit = raw_check_digit_calculation(tms_number[:-1])

    # Check if the calculated check digit matches the given check digit
    return calculated_check_digit == int(tms_number[-1])
