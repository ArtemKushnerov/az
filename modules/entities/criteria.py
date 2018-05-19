from modules.entities.entity import Entity
from modules.entities.value import DateBoundedValue, IntBoundedValue


class Criteria(Entity):

    def __init__(self, dex_date_from=None, dex_date_to=None, apk_size_from=None, apk_size_to=None, vt_detection_from=None, vt_detection_to=None, markets=None, pkg_name=None, sha256=None, sha1=None, md5=None):
        self.dex_date = DateBoundedValue(dex_date_from, dex_date_to)
        self.apk_size = IntBoundedValue(apk_size_from, apk_size_to)
        self.vt_detection = IntBoundedValue(vt_detection_from, vt_detection_to)
        self.markets = set(markets) if markets else None
        self.pkg_name = set(pkg_name) if pkg_name else None
        self.sha256 = set(sha256) if sha256 else None
        self.sha1 = set(sha1) if sha1 else None
        self.md5 = set(md5) if md5 else None

    def _key(self):
        return self.dex_date, self.apk_size, self.vt_detection, self.markets, self.pkg_name, self.sha256, self.sha1, self.md5

    def __str__(self):
        return f'dex_date={self.dex_date}, apk_size={self.apk_size}, vt_detection={self.vt_detection}, markets={self.markets}, pkg_name={self.pkg_name}, sha256={self.sha256}, sha1={self.sha1}, md5={self.md5}'

