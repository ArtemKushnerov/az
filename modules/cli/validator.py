import sys


class Validator:
    def __init__(self, number, dexdate, apksize, vtdetection, markets, pkgname, metadata, sha256, sha1, md5):
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
        self.check_number_is_positive_or_none()
        self._check_only_one_hash_is_used()

    def _check_only_one_hash_is_used(self):
        if (self.sha256 and self.sha1) or (self.sha256 and self.md5) or (self.sha1 and self.md5):
            sys.exit('Please specify only one hashing algorithm')

    def check_number_is_positive_or_none(self):
        if not (self.number > 0 or self.number is None):
            sys.exit('Number of apks must be positive')


