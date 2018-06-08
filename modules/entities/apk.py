from modules.entities.entity import Entity


class MarketsSet(set):
    def __init__(self, markets):
        super().__init__(markets.split('|'))

    def __str__(self):
        return '|'.join(sorted(self))


class Apk(Entity):
    def __init__(self, sha256=None, sha1=None, md5=None, dex_date=None, apk_size=None, pkg_name=None, vercode=None, vt_detection=None, vt_scan_date=None, dex_size=None, markets=None):
        self.sha256 = sha256
        self.sha1 = sha1
        self.vercode = int(vercode) if vercode else None
        self.md5 = md5
        self.dex_date = dex_date  # for performance reasons not parsing date here
        self.apk_size = int(apk_size) if apk_size else None
        self.pkg_name = pkg_name
        self.vt_detection = int(vt_detection) if vt_detection else None
        self.vt_scan_date = vt_scan_date
        self.dex_size = int(dex_size) if dex_size else None
        self.markets = MarketsSet(markets) if markets else None

    def _key(self):
        return self.sha256
