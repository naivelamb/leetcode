"""
https://leetcode.com/problems/is-subsequence/
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        match = 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
                match += 1
            else:
                p2 += 1
        return match == len(s)
