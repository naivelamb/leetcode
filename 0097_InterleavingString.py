# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/interleaving-string/

DFS + memo

dfs(s1, s2, s3) => True if s3 can be interleaved from s1 and s2
memo[(s1, s2, s3)] => True if s3 can be interleaved from s1 and s2
"""

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """        
        if len(s1) + len(s2) != len(s3):
            return False
        cache = {('', '', ''): True}
        def dfs(s1, s2, s3):
            if (s1, s2, s3) in cache:
                return cache[(s1, s2, s3)]
            
            use1 = use2 = False
            if s1 and s1[0] == s3[0]:
                use1 = dfs(s1[1:], s2, s3[1:])
            if s2 and s2[0] == s3[0]:
                use2 = dfs(s1, s2[1:], s3[1:])
            cache[(s1, s2, s3)] = use1 or use2
            return cache[(s1, s2, s3)]
        return dfs(s1, s2, s3)