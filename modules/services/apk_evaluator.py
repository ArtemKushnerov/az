from datetime import datetime


class ApkEvaluator:

    DATE_PATTERN = '%Y-%m-%d %H:%M:%S'

    def __init__(self, criteria=None):
        self.criteria = criteria

    def satisfies(self, apk):
        if not apk:
            return False
        return self.satisfies_markets(apk) and self.satisfies_size(apk) and self.satisfies_date(apk) and self.satisfies_name(apk) and self.satisfies_vt_detection(apk)

    def satisfies_markets(self, apk):
        satisfies = True
        criteria_markets = self.criteria.get('markets')
        if criteria_markets:
            satisfies = apk.markets and criteria_markets.intersection(set(apk.markets))
        return satisfies

    def satisfies_vt_detection(self, apk):
        satisfies = True
        criteria_vt_detection = self.criteria.get('vt_detection')
        if criteria_vt_detection:
            satisfies = self.falls_into_range(apk.vt_detection, criteria_vt_detection)
        return satisfies

    def satisfies_name(self, apk):
        satisfies = True
        criteria_pkg_name = self.criteria.get('pkg_name')
        if criteria_pkg_name:
            satisfies = apk.pkg_name in criteria_pkg_name
        return satisfies

    def satisfies_size(self, apk):
        satisfies = True
        criteria_apk_size = self.criteria.get('apk_size')
        if criteria_apk_size:
            satisfies = self.falls_into_range(apk.apk_size, criteria_apk_size)
        return satisfies

    def satisfies_date(self, apk):
        satisfies = True
        criteria_dex_date = self.criteria.get('dex_date')
        apk_date = datetime.strptime(apk.dex_date, self.DATE_PATTERN) if apk.dex_date else None
        if criteria_dex_date:
            satisfies = self.falls_into_range(apk_date, criteria_dex_date)

        return satisfies

    def falls_into_range(self, value, bounds):
        satisfies = True
        lower = bounds.get('from')
        upper = bounds.get('to')
        if value:
            if lower:
                satisfies = satisfies and lower <= value
            if upper:
                satisfies = satisfies and value <= upper
        else:
            satisfies = False
        return satisfies
