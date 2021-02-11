"""
https://leetcode.com/problems/valid-anagram/
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ref1 = collections.Counter(s)
        ref2 = collections.Counter(t)
        for ch in ref1:
            if ref1[ch] != ref2[ch]:
                return False
        for ch in ref2:
            if ref1[ch] != ref2[ch]:
                return False
        return True