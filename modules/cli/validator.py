from modules.exceptions import ValidationException
from modules.exceptions import NoArgsException


class Validator:
    def __init__(self, number=None, dexdate=None, apksize=None, vtdetection=None, markets=None, pkgname=None, metadata=None, sha256=None, sha1=None, md5=None):
        self.number = number
        self.dexdate = dexdate
        self.apksize = apksize
        self.vtdetection = vtdetection
        self.markets = markets
        self.pkgname = pkgname
        self.metadata = metadata
        self.sha256 = sha256
        self.sha1 = sha1
        self.md5 = md5

    def validate(self):
        self.check_at_least_one_arg_provided()
        self.check_number_is_positive()
        self._check_only_one_hash_is_used()

    def check_at_least_one_arg_provided(self):
        if all(value is None for value in vars(self).values()):
            raise NoArgsException()

    def _check_only_one_hash_is_used(self):
        if (self.sha256 and self.sha1) or (self.sha256 and self.md5) or (self.sha1 and self.md5):
            raise ValidationException('Please specify only one hashing algorithm')

    def check_number_is_positive(self):
        # None means download all
        if not (self.number is None or self.number > 0):
            raise ValidationException('Number of apks must be positive')



