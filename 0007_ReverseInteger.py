"""
https://leetcode.com/problems/reverse-integer/
"""
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        positive = True
        if x < 0:
            positive = False
            x = -x
        while x:
            ans *= 10
            n = x % 10
            ans += n
            x = x // 10

        if not positive:
            ans = -ans

        if ans > 2**31 -1 or ans < -2**31:
            return 0
        else:
            return ans
