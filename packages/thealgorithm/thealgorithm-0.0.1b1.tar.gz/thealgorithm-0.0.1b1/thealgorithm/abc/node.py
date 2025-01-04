class Node:
    def __init__(self, value, _next=None, _prev=None):
        self.value = value
        self.next = _next
        self.prev = _prev

    def __repr__(self) -> str:
        return f"Node({repr(self.value)})"


class PriorityNode(Node):
    def __init__(self, value, _next=None, _prev=None, _priority=None):
        super().__init__(value, _next, _prev)
        if _priority is None:
            _priority = float("-inf")
        self.priority = _priority

    def __repr__(self) -> str:
        return f"PriorityNode({self.priority}: {repr(self.value)})"

    def __lt__(self, other: "PriorityNode") -> bool:
        if self.priority == other.priority:
            return self.value < other.value
        return self.priority < other.priority

    def __gt__(self, other: "PriorityNode") -> bool:
        if self.priority == other.priority:
            return self.value > other.value
        return self.priority > other.priority

    def __eq__(self, other: "PriorityNode") -> bool:
        if self.priority == other.priority:
            return self.value == other.value
        return self.priority == other.priority

    def __le__(self, other: "PriorityNode") -> bool:
        return self < other or self == other

    def __ge__(self, other: "PriorityNode") -> bool:
        return self > other or self == other

    def __ne__(self, other: "PriorityNode") -> bool:
        return not self == other

    def __iter__(self):
        yield self.priority
        yield self.value
