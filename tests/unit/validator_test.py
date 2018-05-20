import unittest

from modules.cli.validator import Validator
from modules.exceptions import ValidationException


class ValidatorTest(unittest.TestCase):

    def test_number(self):
        validator = Validator(number=0)
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(number=-10)
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(number=10)
        validator.validate()

    def test_hashing(self):
        validator = Validator(sha256=5, md5=7, sha1=8)
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(sha256=5, md5=7)
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(sha1=5, md5=7)
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(sha256=5, sha1=7)
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(sha256=5)
        validator.validate()

        validator = Validator()
        validator.validate()


if __name__ == '__main__':
    unittest.main()
