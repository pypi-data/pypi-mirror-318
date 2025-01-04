from collections.abc import Iterable

from .base import ABCIterable
from .node import Node


class Stack(ABCIterable):
    def __init__(self, values=None, size=1000):
        super().__init__()
        self._head = None
        self._max_size = size

        if values is not None:
            if not isinstance(values, Iterable):
                raise TypeError(f"{type(values).__name__} object is not an iterable.")
            self.extend(values)

    def __iter__(self):
        self._curr = self._head
        return self

    def __next__(self):
        if self._curr is None:
            raise StopIteration
        value = self._curr.value
        self._curr = self._curr.next
        return value

    def __del__(self):
        self.clear()

    def push(self, value):
        if not self:
            self._head = Node(value)
            self._size = 1
            return

        if len(self) >= self._max_size:
            raise OverflowError("the stack has reached its maximum capacity.")

        self._head = Node(value, self._head)
        self._size += 1

    def pop(self):
        if not self:
            raise IndexError("pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value

    def peek(self):
        return None if not self else self._head.value

    def clear(self):
        self._size = 0
        self._head = None

    def extend(self, other):
        if not isinstance(other, Iterable):
            raise TypeError(f"{type(other).__name__} object is not an iterable.")

        if len(self) + sum(1 for _ in other) > self._max_size:
            raise OverflowError("The stack has reached its maximum capacity.")

        for value in other:
            self.push(value)
