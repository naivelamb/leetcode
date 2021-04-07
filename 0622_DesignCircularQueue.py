"""
https://leetcode.com/problems/design-circular-queue/

Use list to store values, use head & tail pointer to to locate position. 

Time complexity: 
__init__: O(k)
enQueue: O(1)
deQueue: O(1)
Front: O(1)
Rear: O(1)
isEmpty: O(1)
isFull: O(1)
"""
class MyCircularQueue:

    def __init__(self, k: int):
        self.vals = [-1] * k
        self.head = 0
        self.tail = -1
        self.k = k
        self.n = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.tail += 1
            self.tail = self.tail % self.k
            self.vals[self.tail] = value
            self.n += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.vals[self.head] = -1
            self.head += 1
            self.head = self.head % self.k
            self.n -= 1
            return True

    def Front(self) -> int:
        return self.vals[self.head]

    def Rear(self) -> int:
        return self.vals[self.tail]

    def isEmpty(self) -> bool:
        return (self.n == 0)

    def isFull(self) -> bool:
        return (self.n == self.k)