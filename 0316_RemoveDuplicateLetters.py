# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/remove-duplicate-letters/

When we scan from left to right, we only add character to the ans when it has 
not been seen. 
To make sure we have the smallest in lexicographical, we need to check whether 
the adding character is smaller than the previous character, and the previous 
character can be found in the following string. 
Hence, we need a reference dictionary for the last index of the characters.

Time compelxity: O(n) -> a character is visited at most twice. 
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ref = {ch: i for i, ch in enumerate(s)} # last index ref
        ans = []
        seen = set()
        for i, ch in enumerate(s):
            if ch not in seen: # we only process this case
                while ans and ch < ans[-1] and i < ref[ans[-1]]: # it can be found afterwards
                    tail = ans.pop()
                    seen.remove(tail)
                ans.append(ch)
                seen.add(ch)
        return ''.join(ans)