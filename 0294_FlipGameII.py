# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/flip-game-ii/

DFS + memo
For each string, we check all the possible next move string, see whether we can 
guarantee a win. 

"""
class Solution:
    def canWin(self, s: 'str') -> 'bool':
        self.memo = {}
        return self.dfs(s)
    
    def dfs(self, s):
        # Given s, return True if next mover can gurantee a win.
        if s in self.memo:
            return self.memo[s]
        res = []
        for i in range(len(s) - 1):
            if s[i:i+2] == '++':
                res.append(self.dfs(s[:i] + '--' + s[i+2:]))
        if res:
            self.memo[s] = not all(res)
        else:
            self.memo[s] = False
        return self.memo[s]