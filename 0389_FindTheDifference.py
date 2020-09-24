"""
https://leetcode.com/problems/find-the-difference/

Get the count of chars in s, then check which one is the addition one in t.

Time Complexity: O(N)
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = collections.Counter(s)
        for ch in t:
            if cnt.get(ch, 0) == 0:
                return ch
            else:
                cnt[ch] -= 1
