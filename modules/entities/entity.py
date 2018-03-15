from abc import abstractmethod, ABC


class Entity(ABC):

    @abstractmethod
    def _key(self):
        pass

    def __eq__(self, other):
        return other is not None and self._key() == other._key()

    def __hash__(self):
        return hash(self._key())

    def __str__(self):
        return str(self._key())

    def __repr__(self):
        return self.__str__()
