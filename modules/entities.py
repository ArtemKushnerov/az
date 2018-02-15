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


class Source(Entity):
    def __init__(self, records=None, input_file=None):
        if not records:
            records = []
        self.records = records
        if input_file:
            with open(input_file) as input_file:
                lines = input_file.readlines()
                header = lines[0].strip('\n').split(',')
                for line in lines[1:]:
                    records.append(dict(zip(header, line.strip('\n').replace('"', '').split(','))))
                self.records = input_file.readlines()

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

    def __repr__(self):
        return self.__str__()


class Apk(Entity):
    def __init__(self, pkg_name=None, apk_size=None, dex_date=None, vt_detection=None, markets=None, sha256=None):
        self.apk_size = apk_size
        self.pkg_name = pkg_name
        self.dex_date = None
        if dex_date is not None:
            self.dex_date = parse(dex_date)
        self.vt_detection = vt_detection
        self.markets = markets
        #todo only this field is mandatory
        self.sha256 = sha256

    def _key(self):
        return (self.pkg_name)

    def __str__(self):
        return f'pkg_name:{self.pkg_name}; apk_size:{self.apk_size}'

    def __repr__(self):
        return self.__str__()
