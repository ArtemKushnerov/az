class Parser:
    RANGE_ARGS_DELIMITER = ':'
    LIST_ARGS_DELIMITER = ','
    METADATA_DEFAULT_VALUE = ['sha256', 'pkg_name', 'apk_size', 'dex_date', 'markets']

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

    def parse(self):
        dex_date_from, dex_date_to = self.dexdate.split(self.RANGE_ARGS_DELIMITER) if self.dexdate else (None, None)
        apksize_from, apksize_to = self.apksize.split(self.RANGE_ARGS_DELIMITER) if self.apksize else (None, None)
        vt_detection_from, vt_detection_to = self.vtdetection.split(self.RANGE_ARGS_DELIMITER) if self.vtdetection else (None, None)
        markets = self.markets.split(self.LIST_ARGS_DELIMITER) if self.markets else None
        pkg_name = self.pkgname.split(self.LIST_ARGS_DELIMITER) if self.pkgname else None
        sha256 = self.sha256.split(self.LIST_ARGS_DELIMITER) if self.sha256 else None
        sha1 = self.sha1.split(self.LIST_ARGS_DELIMITER) if self.sha1 else None
        md5 = self.md5.split(self.LIST_ARGS_DELIMITER) if self.md5 else None
        metadata = self.metadata.split(self.LIST_ARGS_DELIMITER) if self.metadata else self.METADATA_DEFAULT_VALUE
        return dex_date_from, dex_date_to, apksize_from, apksize_to, vt_detection_from, vt_detection_to, markets, pkg_name, sha256, sha1, md5, metadata
