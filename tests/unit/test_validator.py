import unittest

from modules.cli.args import Arguments
from modules.cli.validator import Validator
from modules.exceptions import ValidationException, NoArgsException


class ValidatorTest(unittest.TestCase):

    def test_number(self):
        validator = Validator(Arguments(number=0))
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(Arguments(number=-10))
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(Arguments(number=10))
        validator.validate()

    def test_hashing(self):
        validator = Validator(Arguments(sha256=5, md5=7, sha1=8))
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(Arguments(sha256=5, md5=7))
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(Arguments(sha1=5, md5=7))
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(Arguments(sha256=5, sha1=7))
        with self.assertRaises(ValidationException):
            validator.validate()

        validator = Validator(Arguments(sha256=5))
        validator.validate()
        validator = Validator(Arguments(sha1=5))
        validator.validate()
        validator = Validator(Arguments(md5=5))
        validator.validate()

    def test_no_args(self):
        with self.assertRaises(NoArgsException):
            Validator(Arguments()).validate()


if __name__ == '__main__':
    unittest.main()
