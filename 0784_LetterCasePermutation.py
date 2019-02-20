# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/letter-case-permutation/

dfs + backtracking
"""
class Solution:
    def letterCasePermutation_dfs(self, S: 'str') -> 'List[str]':
        S = S.lower()
        mask = []
        for i, c in enumerate(S):
            if c.isalpha(): mask.append(i)
        if not mask:
            return [S]
        
        res = []
        
        def dfs(level, n, idx, curr):
            if level == n:
                res.append(curr)
                return
            for i in range(idx, len(mask)):
                p = mask[i]
                dfs(level + 1, n, i + 1, curr[:p] + curr[p].upper() + curr[p+1:])
        
        for i in range(len(mask) + 1):
            dfs(0, i, 0, S)
        
        return res
    
    def letterCasePermutation(self, S: 'str') -> 'List[str]':
        S = S.lower()
        if len(S) == 1:
            if S.isalpha():
                return [S, S.upper()]
            else:
                return [S]
        
        res = [S]
        for i in range(len(S)):
            if S[i].isalpha():
                for j in range(len(res)):
                    change_alpha = res[j][:i] + res[j][i].upper() + res[j][i + 1:]
                    res.append(change_alpha)
        return res
