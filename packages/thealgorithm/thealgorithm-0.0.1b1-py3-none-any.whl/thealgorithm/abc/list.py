from collections.abc import Iterable

from .base import MutSequence, ABCIterable
from .node import Node


class LinearList(MutSequence, ABCIterable):
    def __init__(self, *values):
        super().__init__()
        self._head = None

        if len(values) == 1:
            if not isinstance(values[0], Iterable):
                raise TypeError(f"{type(values[0]).__name__} object is not iterable")
            elif isinstance(values[0], Iterable):
                self.extend(values[0])
        else:
            self.extend(values)

    def __repr__(self):
        return f"[{' '.join(map(str, self))}]"

    def __iter__(self):
        self._curr = self._head
        return self

    def __next__(self):
        if self._curr is None:
            raise StopIteration
        value = self._curr.value
        self._curr = self._curr.next
        return value

    def __delitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("llist.__delitem__(index): index out of range.")
        self.pop(index)

    def __get_node(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("llist.__get_node(index): index out of range.")
        curr = self._head
        for _ in range(index):
            curr = curr.next
        return curr

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index >= self._size:
                raise IndexError("llist[index]: index out of range.")
            return self.__get_node(index).value

        elif isinstance(index, slice):
            start, stop, step = index.indices(self._size)
            result = []
            for i in range(start, stop, step):
                result.append(self.__get_node(i).value)
            return LinearList(result)
        else:
            raise TypeError("Invalid argument type.")

    def __setitem__(self, index, value):
        if index < 0 or index >= self._size:
            raise IndexError("llist[index]: index out of range.")

        self.__get_node(index).value = value

    def clear(self):
        self._head = None
        self._size = 0

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("llist.get(index): index out of range.")
        return self.__get_node(index).value

    def push(self, value):
        self._head = Node(value, _next=self._head)
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index >= len(self):
            raise IndexError("llist.insert(index, value): index out of range.")
        _curr = _prev = self._head
        for _ in range(index - 1):
            _prev = _curr
            _curr = _curr.next
        _new = Node(value)

        # insert at the end of the list
        if _curr is None:
            _prev.next = _new
        else:
            _next = _curr.next
            # if it has any item next to current index
            if _next:
                _new.next = _next
            _curr.next = _new
        self._size += 1

    def append(self, value):
        new_node = Node(value)
        if not self._head:
            self._head = new_node
        else:
            curr = self._head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def pop(self, index=None):
        if not self._size:
            raise IndexError("pop from empty LinearList")
        index = index if index is not None else self._size - 1
        if index == 0:
            value = self._head.value
            self._head = self._head.next
        else:
            prev = self.__get_node(index - 1)
            value = prev.next.value
            prev.next = prev.next.next
        self._size -= 1
        return value

    def remove(self, value):
        index = self.find(value)
        if index == -1:
            raise ValueError("llist.remove(item): item not in llist")
        self.pop(index)

    def replace(self, index, value):
        if index < 0 or index >= len(self):
            raise IndexError("llist.replace(index, value): index out of range.")
        target = self.__get_node(index)
        target.value = value

    def swap(self, from_i, to_i):
        if from_i == to_i:
            return
        if not (0 <= from_i < len(self)) or not (0 <= to_i < len(self)):
            raise IndexError("llist.swap(from_i, to_i): index out of range.")

        _from, _to = self.__get_node(from_i), self.__get_node(to_i)
        _from.value, _to.value = _to.value, _from.value

    def extend(self, other):
        if not isinstance(other, Iterable):
            raise TypeError(f"{type(other).__name__} object is not an iterable.")
        for value in other:
            self.append(value)


class DoublyList(MutSequence, ABCIterable):
    def __init__(self, *values):
        super().__init__()
        self._head = None
        self._tail = None

        if len(values) == 1:
            if not isinstance(values[0], Iterable):
                raise TypeError(f"{type(values[0]).__name__} object is not iterable")
            elif isinstance(values[0], Iterable):
                self.extend(values[0])
        else:
            self.extend(values)

    def __repr__(self):
        return f"[{' '.join(map(str, self))}]"

    def __iter__(self):
        self._curr = self._head
        return self

    def __next__(self):
        if self._curr is None:
            raise StopIteration
        value = self._curr.value
        self._curr = self._curr.next
        return value

    def __get_node(self, index):
        # negative index is allow.
        if not self._is_valid_index(index):
            raise IndexError("dlist.__get_node(index): index out of range.")

        _curr = self._head
        if index < 0:
            index += len(self)
        for _ in range(index):
            _curr = _curr.next
        return _curr

    def __getitem__(self, index):
        if isinstance(index, int):
            if not self._is_valid_index(index):
                raise IndexError("dlist[index]: index out of range.")
            if index < 0:
                index += len(self)
            return self.__get_node(index).value

        elif isinstance(index, slice):
            start, stop, step = index.indices(self._size)
            result = []
            for i in range(start, stop, step):
                result.append(self.__get_node(i).value)
            return DoublyList(result)
        else:
            raise TypeError("Invalid argument type.")

    def __setitem__(self, index, value):
        if not self._is_valid_index(index):
            raise IndexError("dlist[index]: index out of range.")
        if index < 0:
            index += len(self)
        self.__get_node(index).value = value

    def __delitem__(self, index):
        if not self._is_valid_index(index):
            raise IndexError("dlist.__delitem__(index): index out of range.")
        self.pop(index)

    def _is_valid_index(self, index):
        return -len(self) <= index < len(self)

    def get(self, index):
        if not self._is_valid_index(index):
            raise IndexError("dlist.get(index): index out of range.")
        return self.__get_node(index).value

    def clear(self):
        self._size = 0
        self._head = None
        self._tail = None

    # add new item at the top
    def push(self, value):
        _new = Node(value, _next=self._head)
        if not self:
            self._head = self._tail = _new
            self._size += 1
            return

        _new.prev = _new
        self._head = _new
        self._size += 1

    # add new item at the bottom
    def append(self, value):
        _new = Node(value)
        if not self:
            self._head = self._tail = _new
            self._size += 1
            return

        _prev = self._tail
        _prev.next = _new
        _new.prev = _prev
        self._tail = _new
        self._size += 1

    def insert(self, index, value):
        if index in {0, -len(self)}:  # Insert at the head
            self.push(value)
        elif index >= len(self) or index == -1:  # Insert at the tail
            self.append(value)
        else:
            _new = Node(value)
            _curr = self._head
            if index < 0:
                index += len(self)
            for _ in range(index):
                _curr = _curr.next

            _new.next = _curr
            _new.prev = _curr.prev
            _curr.prev.next = _new
            _curr.prev = _new

            self._size += 1

    def pop(self, index=None):
        if not self._size:
            raise IndexError("pop from empty DoublyList")
        index = index if index is not None else self._size - 1
        node = self.__get_node(index)
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self._head:
            self._head = node.next
        if node == self._tail:
            self._tail = node.prev
        self._size -= 1
        return node.value

    def remove(self, value):
        index = self.find(value)
        if index == -1:
            raise ValueError("dlist.remove(item): item not in llist")
        self.pop(index)

    def replace(self, index, value):
        if not self._is_valid_index(index):
            raise IndexError("dlist.replace(index, value): Index out of range.")
        target = self.__get_node(index)
        target.value = value

    def swap(self, from_i, to_i):
        if from_i == to_i:
            return
        if not self._is_valid_index(from_i) or not self._is_valid_index(to_i):
            raise IndexError("dlist.swap(from_i, to_i): index out of range.")

        _from, _to = self.__get_node(from_i), self.__get_node(to_i)
        _from.value, _to.value = _to.value, _from.value

    def extend(self, other):
        if not isinstance(other, Iterable):
            raise TypeError(f"{type(other).__name__} object is not an iterable.")
        for value in other:
            self.append(value)
