from modules.entities.apk import Apk
from modules.entities.entity import Entity


class Source(Entity):
    def __init__(self, input_file=None):
        self.input_file = open(input_file)
        next(self.input_file) # skip header

    def __iter__(self):
        return self

    def __next__(self):
        try:
            line = next(self.input_file)
        except StopIteration:
            self.input_file.close()
            raise StopIteration
        columns = line.strip('\n').replace('"', '').split(',')
        return Apk(*columns)

    def _key(self):
        pass

