"""
https://leetcode.com/problems/first-unique-character-in-a-string/
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ref = {}
        for ch in s:
            ref[ch] = ref.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if ref[ch] == 1:
                return i
        return -1
