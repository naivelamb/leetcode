"""
https://leetcode.com/problems/reverse-bits/
"""
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = "{0:032b}".format(n)
        binary_re = binary[::-1]
        return int(binary_re, 2)
