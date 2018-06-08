from modules.exceptions import ValidationException
from modules.exceptions import NoArgsException


class Validator:
    def __init__(self, args):
        self.args = args

    def validate(self):
        self._check_at_least_one_arg_provided()
        self._check_number_is_positive()
        self._check_only_one_hash_is_used()

    def _check_at_least_one_arg_provided(self):
        if all(value is None for value in vars(self.args).values()):
            raise NoArgsException()

    def _check_only_one_hash_is_used(self):
        if (self.args.sha256 and self.args.sha1) or (self.args.sha256 and self.args.md5) or (self.args.sha1 and self.args.md5):
            raise ValidationException('Please specify only one hashing algorithm')

    def _check_number_is_positive(self):
        # None means download all
        if not (self.args.number is None or self.args.number > 0):
            raise ValidationException('Number of apks must be positive')



