"""
https://leetcode.com/problems/add-digits/

Convert to 9-base
"""
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return num % 9 if num%9 != 0 else 9
