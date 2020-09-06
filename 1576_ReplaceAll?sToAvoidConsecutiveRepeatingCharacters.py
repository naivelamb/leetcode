"""
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

The letter only need to be one of abc.
Time Complexity: O(N)
"""
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i, ch in enumerate(s):
            if ch == '?':
                for c in 'abc':
                    if (i == 0 or s[i-1] != c) and (i+1 == len(s) or s[i+1] != c):
                        s[i] = c
                        break
        return ''.join(s)
