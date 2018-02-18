from modules.entities.entity import Entity


class Apk(Entity):
    def __init__(self, sha256=None, sha1=None, md5=None, dex_date=None, apk_size=None, pkg_name=None, vercode=None, vt_detection=None, vt_scan_date=None, dex_size=None, markets=None):
        self.sha256 = sha256
        self.sha1 = sha1
        self.vercode = int(vercode) if vercode else None
        self.md5 = md5
        self.dex_date = dex_date
        self.apk_size = int(apk_size) if apk_size else None
        self.pkg_name = pkg_name
        self.vt_detection = int(vt_detection) if vt_detection else None
        self.vt_scan_date = vt_scan_date
        self.dex_size = int(dex_size) if dex_size else None
        self.markets = markets.split('|') if markets else None

    def _key(self):
        return (self.sha256)

    def __str__(self):
        return f'pkg_name={self.pkg_name},dex_date={self.dex_date},markets={self.markets}'

    def __repr__(self):
        return self.__str__()
