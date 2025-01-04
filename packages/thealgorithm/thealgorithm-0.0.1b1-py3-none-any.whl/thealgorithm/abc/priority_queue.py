from .node import PriorityNode
from .queue import Queue
from .base import Sequence


class PriorityQueue(Queue, Sequence):
    def __init__(self, iterable=None, size=1000):
        super().__init__(size=size)
        if iterable is not None:
            self.extend(iterable)

    def __getitem__(self, index: int) -> PriorityNode:
        if index < 0 or index >= self._size:
            raise IndexError("priority_queue.__getitem__(index): index out of range.")
        _curr = self._head
        for _ in range(index):
            _curr = _curr.next
        return _curr

    def __repr__(self):
        _str = "PriorityQueue("
        for i in range(self._size):
            _str += f"{self[i].priority}: {self[i].value}, "
        return _str.rstrip(", ") + ")"

    def peek(self):
        if not self:
            return None
        return self._head.value

    def dequeue(self):
        if not self:
            raise IndexError("dequeue from empty priority_queue")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value

    def enqueue(self, value, priority=None):
        if len(self) >= self._max_size:
            raise OverflowError("The priority_queue has reached its maximum capacity.")

        new = PriorityNode(value=value, _priority=priority)

        if not self:
            self._head = self._tail = new
        else:
            _curr = self._head
            _prev = None
            while _curr and _curr.priority >= priority:
                _prev = _curr
                _curr = _curr.next

            if _prev is None:
                new.next = self._head
                self._head.prev = new
                self._head = new
            elif _curr is None:
                self._tail.next = new
                new.prev = self._tail
                self._tail = new
            else:
                _prev.next = new
                new.prev = _prev
                new.next = _curr
                _curr.prev = new

        self._size += 1

    def extend(self, other):
        if not isinstance(other, Sequence):
            raise TypeError(f"{type(other).__name__} object is not iterable.")

        if len(self) + len(other) > self._max_size:
            raise OverflowError("The priority_queue has reached its maximum capacity.")

        for item in other:
            if isinstance(item, (tuple, list, dict)) and len(item) == 2:
                priority, value = item
            else:
                priority, value = None, item

            self.enqueue(value, priority=priority)
