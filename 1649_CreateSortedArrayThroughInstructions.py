"""
https://leetcode.com/problems/create-sorted-array-through-instructions/

Segment tree, use Binary Indexed Tree here.

Time complexity: O(NlogM), M is the range of instructions[i]
"""
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        m = max(instructions)
        c = [0] * (m + 1)

        def update(x):
            while (x <= m):
                c[x] += 1
                x += x & -x
        
        def get(x):
            res = 0
            while (x > 0):
                res += c[x]
                x -= x & -x
            return res
        
        res = 0
        for i, a in enumerate(instructions):
            res += min(get(a - 1), i - get(a))
            update(a)
        return res % (10 ** 9 + 7)