import sys


class Validator:
    def __init__(self, dexdate, apksize, vtdetection, markets, pkgname, metadata, sha256, sha1, md5):
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
        self._check_only_one_hash_is_used()

    def _check_only_one_hash_is_used(self):
        if not {None, None} in {self.sha256, self.sha1, self.md5}:
            sys.exit('Please specify only one hashing algorithm')
