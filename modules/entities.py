from abc import abstractmethod, ABC
from dateutil.parser import parse


class Entity(ABC):

    @abstractmethod
    def _key(self):
        pass

    def __eq__(self, other):
        return other is not None and self._key() == other._key()

    def __hash__(self):
        return hash(self._key())


class Criteria(Entity):
    def __init__(self, dex_date=None, apk_size=None, pkg_name=None, vt_detection=None, markets=None):
        self.dex_date = dex_date
        self.apk_size = apk_size
        self.pkg_name = pkg_name
        self.vt_detection = vt_detection
        self.markets = markets

    def _key(self):
        pass


class Source(Entity):
    def __init__(self, records):
        self.records = records

    def _key(self):
        pass

    def __iter__(self):
        return iter(self.records)


class Record(Entity):
    def __init__(self, line):
        self.columns = line.split(',')


class Dataset(Entity):
    def __init__(self, *apks):
        if apks is None:
            apks = tuple()
        self.apks = tuple(apks)

    def _key(self):
        return frozenset(self.apks)

    def add(self, apk):
        self.apks = (*self.apks, apk)

    def __str__(self):
        return str(self.apks)

    def __len__(self):
        return len(self.apks)

    def __iter__(self):
        return iter(self.apks)

    def contains(self, subset):
        return set(subset.apks).issubset(set(self.apks))

    def is_empty(self):
        return len(self.apks) == 0

class Metadata(Entity):

    def _key(self):
        pass


class Apk(Entity):
    def __init__(self,pkg_name=None, apk_size=None, dex_date=None, vt_detection=None, markets=None):
        self.apk_size = apk_size
        self.pkg_name = pkg_name
        self.dex_date = None
        if dex_date is not None:
            self.dex_date = parse(dex_date)
        self.vt_detection = vt_detection
        self.markets = markets

    def satisfies(self, criteria):
        satisfies = True
        if criteria.dex_date is not None:
            satisfies = satisfies and self.dex_date is not None and parse(criteria.dex_date.get('from')) < self.dex_date < parse(criteria.dex_date.get('to'))
        if criteria.apk_size is not None:
            satisfies = satisfies and criteria.apk_size.get('from') < self.apk_size < criteria.apk_size.get('to')
        if criteria.pkg_name is not None:
            satisfies = satisfies and self.pkg_name in criteria.pkg_name
        if criteria.vt_detection is not None:
            satisfies = satisfies and criteria.vt_detection.get('from') < self.vt_detection < criteria.vt_detection.get('to')
        if criteria.vt_detection is not None:
            satisfies = satisfies and criteria.markets.intersection(self.markets)
        return satisfies

    def _key(self):
        return (self.pkg_name)

    def __str__(self):
        return f' pkg_name:{self.pkg_name};apk_size:{self.apk_size}'

    def __repr__(self):
        return self.__str__()
