from enum import Enum, auto


class DownloadType(Enum):
    ALL = auto()

    def __str__(self):
        return self.name
