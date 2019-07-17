from modules.entities.apk import Apk
from modules.entities.entity import Entity
import csv


class Source(Entity):
    def __init__(self, input_file=None):
        if isinstance(input_file, str):
            self.input_file = open(input_file)
        else:
            self.input_file = input_file
        self.reader = csv.reader(self.input_file)
        next(self.reader) # skip header

    def __iter__(self):
        return self

    def __next__(self):
        try:
            line = next(self.reader)
        except StopIteration:
            self.input_file.close()
            raise StopIteration
        return Apk(*line)

    def _key(self):
        pass

