# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

Compare one by one.

Time complexity: O(mn), n -> len(d), m -> max(len(x) for x in d)
"""
class Solution:
    def findLongestWord(self, s, d):
        def helper(s, t):
            # is t a substring of s?
            m, n = len(s), len(t)
            if n > m:
                return False
            i, j = 0, 0
            while i < m and j < n:
                if s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return j == n
        
        ans = ''
        for t in d:
            if helper(s, t):
                if len(t) > len(ans):
                    ans = t
                elif len(t) == len(ans):
                    ans = sorted([ans, t])[0]
        return ans        
