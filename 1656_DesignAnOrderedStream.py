"""
https://leetcode.com/problems/design-an-ordered-stream/

Use a pre-defined array to store pairs. Then do as described.

Time complexity: O(N)
"""
class  OrderedStream:
    def __init__(self, n: int):
        self.vals = [''] * (n + 1)
        self.pt = 1

    def insert(self, id: int, value: str) -> List[str]:
        ans = []
        self.vals[id] = value
        if self.pt == id:
            while self.pt < len(self.vals) and self.vals[self.pt] != '':
                ans.append(self.vals[self.pt])
                self.pt += 1
        return ans