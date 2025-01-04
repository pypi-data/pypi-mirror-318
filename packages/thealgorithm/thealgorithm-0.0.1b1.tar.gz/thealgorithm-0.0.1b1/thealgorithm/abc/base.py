from ..sorting import quick

from collections.abc import Iterable, Sequence


class ABCIterable(Iterable):
    def __init__(self, size=0):
        self._size = size

    def __len__(self):
        return self._size

    def __iter__(self):
        raise NotImplementedError("__iter__() method is not implemented yet")

    def __bool__(self):
        return len(self) != 0

    def __del__(self):
        self.clear()

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(str(var) for var in self)})"

    def clear(self):
        raise NotImplementedError("clear() method is not implemented yet")


class ABCSequence(ABCIterable, Sequence):
    def __getitem__(self, index):
        raise NotImplementedError("__getitem__() method is not implemented yet")

    def __eq__(self, other):
        if not isinstance(other, ABCSequence):
            return False
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __contains__(self, value):
        return self.find(value) >= 0

    def find(self, value):
        if not self:
            return -1
        for i, element in enumerate(self):
            if element == value:
                return i
        return -1


class MutSequence(ABCSequence):
    def sort(self, reverse: bool = False):
        quick(self, 0, len(self) - 1, reverse)
