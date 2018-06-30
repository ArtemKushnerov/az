from dateutil.parser import parse

from modules.entities.entity import Entity


class BoundedValue(Entity):
    def __init__(self, lower, upper, preprocess=None):
        if preprocess:
            lower = preprocess(lower) if lower else None
            upper = preprocess(upper) if upper else None
        self.lower = lower
        self.upper = upper

    def _key(self):
        return self.lower, self.upper

    def __bool__(self):
        return True if self.lower is not None or self.upper is not None else False


class DateBoundedValue(BoundedValue):
    def __init__(self, lower, upper):
        super().__init__(lower, upper, preprocess=parse)


class IntBoundedValue(BoundedValue):
    def __init__(self, lower, upper):
        super().__init__(lower, upper, preprocess=int)

