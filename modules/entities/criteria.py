from modules.entities.entity import Entity
from modules.entities.value import DateBoundedValue, IntBoundedValue


class Criteria(Entity):

    def __init__(self, dex_date_from=None, dex_date_to=None, apk_size_from=None, apk_size_to=None, vt_detection_from=None, vt_detection_to=None, markets=None, pkg_name=None):
        self.dex_date = DateBoundedValue(dex_date_from, dex_date_to)
        self.apk_size = IntBoundedValue(apk_size_from, apk_size_to)
        self.vt_detection = IntBoundedValue(vt_detection_from, vt_detection_to)
        self.markets = set(markets) if markets else None
        self.pkg_name = set(pkg_name) if pkg_name else None

    @classmethod
    def init_from_dict(cls, config_dict=None):
        criteria = Criteria()
        #rewrite with blabla if field else None, which is more elegans
        if config_dict:
            dex_date = config_dict.get('dex_date')
            if dex_date:
                criteria.dex_date = DateBoundedValue(dex_date.get('from'), dex_date.get('to'))

            apk_size = config_dict.get('apk_size')
            if apk_size:
                criteria.apk_size = IntBoundedValue(apk_size.get('from'), apk_size.get('to'))

            vt_detection = config_dict.get('vt_detection')
            if vt_detection:
                criteria.vt_detection = IntBoundedValue(vt_detection.get('from'), vt_detection.get('to'))

            markets = config_dict.get('markets')
            if markets:
                criteria.markets = set(markets)

            pkg_name = config_dict.get('pkg_name')
            if pkg_name:
                criteria.pkg_name = set(pkg_name)
        return criteria

    def _key(self):
        return self.dex_date, self.apk_size, self.vt_detection, self.markets, self.pkg_name

    def __str__(self):
        return f'dex_date={self.dex_date}, apk_size={self.apk_size}, vt_detection={self.vt_detection}, markets={self.markets}, pkg_name={self.pkg_name}'

