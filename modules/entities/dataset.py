from modules.entities.entity import Entity


class Dataset(Entity):
    def __init__(self, *apks):
        if apks is None:
            apks = []
        self.apks = list(apks)

    def _key(self):
        return frozenset(self.apks)

    def add(self, apk):
        self.apks.append(apk)

    def __len__(self):
        return len(self.apks)

    def __iter__(self):
        return iter(self.apks)

    def contains(self, subset):
        return set(subset.apks).issubset(set(self.apks))

    def is_empty(self):
        return len(self.apks) == 0
