"""
https://leetcode.com/problems/valid-palindrome/
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s0 = ''
        for c in s:
            if c.isalpha() or c.isdigit():
                s0 += c.lower()
        return s0 == s0[::-1]
