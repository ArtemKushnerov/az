import unittest

from modules.cli.validator import Validator


class ValidatorTest(unittest.TestCase):

    def test_number_is_positive(self):
        validator = Validator(number=-1)
        validator.validate()

if __name__ == '__main__':
    unittest.main()
