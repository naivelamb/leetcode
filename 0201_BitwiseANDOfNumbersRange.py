"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n = n&(n-1)
        return m&n

sol = Solution()
assert sol.rangeBitwiseAnd(5, 7) == 4
assert sol.rangeBitwiseAnd(0, 1) == 0
