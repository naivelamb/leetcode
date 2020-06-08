"""
https://leetcode.com/problems/power-of-two/
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n:
            r = n%2
            n = n//2
            if n == 0 and r == 1:
                return True
            if n != 0 and r == 1:
                return False
        return False
