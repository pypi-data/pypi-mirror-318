from .base import MutSequence
import ctypes


class Array(MutSequence):
    def __init__(self, ctype, size, iterable=None):
        super().__init__(size)
        self.ctype = ctype
        self.array = (ctype * size)()
        self.current_size = 0
        if iterable:
            self.extend(iterable)

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range.")
        self.array[index] = value

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range.")
        try:
            value = self.array[index]
            return value
        except ValueError as e:
            if e.args[0] == "PyObject is NULL":
                raise IndexError("Index out of range.") from e
        except Exception:
            raise NotImplemented("Array.__getitem__() is not implemented yet.")

    def __iter__(self):
        for i in range(self.current_size):
            yield self.array[i]

    def extend(self, iterable):
        if self.current_size + len(iterable) > self._size:
            raise OverflowError("Cannot extend beyond the fixed size of the array.")

        for i, value in enumerate(iterable):
            self.array[self.current_size + i] = value
        self.current_size += len(iterable)

    def clear(self):
        for i in range(self._size):
            self.array[i] = self.ctype()
        self.current_size = 0
