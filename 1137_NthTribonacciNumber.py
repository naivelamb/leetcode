"""
https://leetcode.com/problems/n-th-tribonacci-number/
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            n -= 3
            while n >= 0:
                new_c = a + b + c
                a, b = b, c
                c = new_c
                n -= 1
            return c

sol = Solution()
assert sol.tribonacci(4) == 4
assert sol.tribonacci(25) == 1389537
