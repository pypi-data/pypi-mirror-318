import unittest
import csv
import os
import time
import platform
from KiwiRail_TMS_Checkdigit.tms_checkdigit import calculate_check_digit, is_check_digit_valid


class TestTMSCheckDigit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.examples = []
        cls.not_tms_examples = []
        with open(os.path.join("tests", "tms_numbers.csv"), "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                example = row[0]
                cls.examples.append(example)
        with open(os.path.join("tests", "not_tms_numbers.csv"), "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                example = row[0]
                cls.not_tms_examples.append(example)

    def test_calculate_check_digit(self):
        for example in self.examples:
            with self.subTest(example=example):
                check_digit = calculate_check_digit(example[:-1])
                self.assertEqual(check_digit, int(example[-1]))
                
    def test_tms_valid(self):
        for example in self.examples:
            with self.subTest(example=example):
                valid = is_check_digit_valid(example)
                self.assertEqual(valid, True)

    def test_not_tms_numbers(self):
        for example in self.not_tms_examples:
            with self.subTest(example=example):
                # try:
                valid = is_check_digit_valid(example)
                self.assertEqual(valid, False)
                # except (ValueError, IndexError):
                #     pass

    def test_speed(self):
        print(
            f"\nSystem Specs: OS={platform.system()}, Processor={platform.processor()}, Architecture={platform.machine()}, CPU Count={os.cpu_count()}, Python={platform.python_version()}"
        )

        start_time = time.time()
        iterations = 0
        while time.time() - start_time < 0.1:
            for example in self.examples:
                calculate_check_digit(example[:-1])
                iterations += 1
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(
            f"Performance Results: {iterations} iterations in {(elapsed_time*1000):.0f}ms, Average time per iteration: {(elapsed_time / iterations) * (1000000):.1f}us"
        )


if __name__ == "__main__":
    unittest.main()
