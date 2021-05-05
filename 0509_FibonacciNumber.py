"""
https://leetcode.com/problems/fibonacci-number/
"""
class Solution:
    def fib(self, n: int) -> int:
        self.res = {
            0:0,
            1:1
        }
        def dp(i):
            if i in self.res:
                return self.res[i]
            return dp(i-1) + dp(i-2)
        return dp(n)