"""
https://leetcode.com/problems/power-of-four/
"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num != 0 and num&(num-1) == 0 and len('{0:b}'.format(num)) % 2 == 1
