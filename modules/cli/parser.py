from modules.cli.user_config import UserConfig
from modules.enums import DownloadType


class Parser:
    RANGE_ARGS_DELIMITER = ':'
    LIST_ARGS_DELIMITER = ','
    METADATA_DEFAULT_VALUE = ['sha256', 'pkg_name', 'apk_size', 'dex_date', 'markets']

    def __init__(self, args):
        self.args = args

    def parse(self):
        number = int(self.args.number) if self.args.number else DownloadType.ALL
        dex_date_from, dex_date_to = self.args.dexdate.split(self.RANGE_ARGS_DELIMITER) if self.args.dexdate else (None, None)
        apksize_from, apksize_to = self.args.apksize.split(self.RANGE_ARGS_DELIMITER) if self.args.apksize else (None, None)
        vt_detection_from, vt_detection_to = self.args.vtdetection.split(self.RANGE_ARGS_DELIMITER) if self.args.vtdetection else (None, None)
        markets = self.args.markets.split(self.LIST_ARGS_DELIMITER) if self.args.markets else None
        pkg_name = self.args.pkgname.split(self.LIST_ARGS_DELIMITER) if self.args.pkgname else None
        sha256 = self.get_hash_list(self.args.sha256) if self.args.sha256 else None
        sha1 = self.get_hash_list(self.args.sha1) if self.args.sha1 else None
        md5 = self.get_hash_list(self.args.md5) if self.args.md5 else None
        metadata = self.args.metadata.split(self.LIST_ARGS_DELIMITER) if self.args.metadata else self.METADATA_DEFAULT_VALUE
        key, input_file = self.args.key, self.args.input_file
        if not key or not input_file:
            user_config = UserConfig(key, input_file)
            input_file = input_file if input_file else user_config.in_file
            key = key if key else user_config.key

        return number, dex_date_from, dex_date_to, apksize_from, apksize_to, vt_detection_from, vt_detection_to, markets, pkg_name, sha256, sha1, md5, metadata, key, input_file

    def get_hash_list(self, apk_hashes):
        return [apk_hash.upper() for apk_hash in apk_hashes.split(self.LIST_ARGS_DELIMITER)]