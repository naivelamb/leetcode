"""
https://leetcode.com/problems/lru-cache/

Search -> hashmap.
Use a linked list to maintain the order. The next node of head is the least used one. So when we insert, we put a node at the position previous of the tail.

Time complexity: O(1) for both get() and put()
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ref = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, next1 = node.prev, node.next
        prev.next = next1
        next1.prev = prev

    def _insert(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail

    def get(self, key: int) -> int:
        if key in self.ref:
            node = self.ref[key]
            self._remove(node)
            self._insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.ref:
            self._remove(self.ref[key])
        node = Node(key, value)
        self._insert(node)
        self.ref[key] = node
        if len(self.ref) > self.capacity:
            last = self.head.next
            self._remove(last)
            del self.ref[last.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
