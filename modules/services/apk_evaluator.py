from datetime import datetime


class ApkEvaluator:

    DATE_PATTERN = '%Y-%m-%d %H:%M:%S'

    def __init__(self, criteria=None):
        self.criteria = criteria

    def satisfies(self, apk):
        if not apk:
            return False
        return self.satisfies_sha256(apk) and self.satisfies_sha1(apk) and self.satisfies_md5(apk) and self.satisfies_markets(apk) and self.satisfies_size(apk)\
            and self.satisfies_date(apk) and self.satisfies_name(apk) and self.satisfies_vt_detection(apk)

    def satisfies_markets(self, apk):
        satisfies = True
        if self.criteria.markets:
            satisfies = apk.markets and self.criteria.markets.intersection(apk.markets)
        return satisfies

    def satisfies_sha256(self, apk):
        satisfies = True
        if self.criteria.sha256:
            satisfies = apk.sha256 in self.criteria.sha256
        return satisfies

    def satisfies_sha1(self, apk):
        satisfies = True
        if self.criteria.sha1:
            satisfies = apk.sha1 in self.criteria.sha1
        return satisfies

    def satisfies_md5(self, apk):
        satisfies = True
        if self.criteria.md5:
            satisfies = apk.md5 in self.criteria.md5
        return satisfies

    def satisfies_vt_detection(self, apk):
        satisfies = True
        if self.criteria.vt_detection:
            satisfies = self.satisfies_bounds(apk.vt_detection, self.criteria.vt_detection)
        return satisfies

    def satisfies_name(self, apk):
        satisfies = True
        if self.criteria.pkg_name:
            satisfies = apk.pkg_name in self.criteria.pkg_name
        return satisfies

    def satisfies_size(self, apk):
        satisfies = True
        if self.criteria.apk_size:
            satisfies = self.satisfies_bounds(apk.apk_size, self.criteria.apk_size)
        return satisfies

    def satisfies_date(self, apk):
        satisfies = True
        apk_date = datetime.strptime(apk.dex_date, self.DATE_PATTERN) if apk.dex_date else None
        if self.criteria.dex_date:
            satisfies = self.satisfies_bounds(apk_date, self.criteria.dex_date)

        return satisfies

    @staticmethod
    def satisfies_bounds(value, bounded_value):
        satisfies = True
        if value is not None:
            if bounded_value.lower is not None:
                satisfies = satisfies and bounded_value.lower <= value
            if bounded_value.upper is not None:
                satisfies = satisfies and value <= bounded_value.upper
        else:
            satisfies = False
        return satisfies
