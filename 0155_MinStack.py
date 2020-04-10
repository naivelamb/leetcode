"""
https://leetcode.com/problems/min-stack/
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.vals = []
        self.ans = []

    def push(self, x: int) -> None:
        self.vals.append(x)
        if self.ans:
            self.ans.append(min(x, self.ans[-1]))
        else:
            self.ans.append(x)

    def pop(self) -> None:
        self.vals.pop()
        self.ans.pop()

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.ans[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
