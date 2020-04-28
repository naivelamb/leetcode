"""
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3313/

Use linked list to maintain the order of unique numbers.
A hashmap to record the unique number, point to the node in linked list.
A hashmap to record the count of numbers

__init__() -> O(n)
show() -> O(1)
add() -> O(1)
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class FirstUnique:

    def __init__(self, nums):
        # init linked list
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # check nums
        self.cnt_ref = {}
        self.ref = {}
        for n in nums:
            self.add(n)

    def _insert(self, value) -> None:
        """Insert at tail"""
        node = Node(value)
        node.next = self.tail
        node.prev = self.tail.prev
        node.prev.next = node
        node.next.prev = node
        self.ref[value] = node
        self.cnt_ref[value] = 1

    def _del(self, value) -> None:
        """remove a node"""
        node = self.ref[value]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.ref[value]

    def showFirstUnique(self) -> int:
        if self.ref:
            return self.head.next.val
        else:
            return -1

    def add(self, value: int) -> None:
        if value in self.cnt_ref:
            self.cnt_ref[value] += 1
            if value in self.ref:
                self._del(value)
        else:
            self._insert(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
