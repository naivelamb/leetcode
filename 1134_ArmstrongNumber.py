"""
https://leetcode.com/problems/armstrong-number/
"""
class Solution:
    def isArmstrong(self, n: int) -> bool:
        s = str(n)
        k = len(s)
        res = sum(int(x) ** k for x in s)
        return res == n