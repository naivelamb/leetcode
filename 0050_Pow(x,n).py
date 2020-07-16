"""
https://leetcode.com/problems/powx-n/
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            x = 1/x
            n = -n
        return self.helper(x, n)

    def helper(self, x, n):
        if n == 0:
            return 1.0
        half = self.helper(x, n//2)
        if n % 2 == 0:
            return half**2
        else:
            return half**2*x
