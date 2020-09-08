"""
https://leetcode.com/problems/moving-average-from-data-stream/

Use deque to store data. Keep track of total sum, number of elements.

Time Complexity: O(1) for next()
"""
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.vals = collections.deque()
        self.size = size
        self.n = 0
        self.val = 0

    def next(self, val: int) -> float:
        if self.n == self.size:
            # remove
            self.val -= self.vals.popleft()
            self.val += val
            self.vals.append(val)
        else:
            self.vals.append(val)
            self.val += val
            self.n += 1
        return self.val/self.n


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
