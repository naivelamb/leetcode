"""
https://leetcode.com/problems/length-of-last-word/
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        while s and s[-1] == "":
            s.pop()
        if s and s[-1]:
            return len(s[-1])
        else:
            return 0
