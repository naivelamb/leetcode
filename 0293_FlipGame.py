# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/flip-game/

Find consecutive '+', replace them.
"""
class Solution:
    def generatePossibleNextMoves(self, s: 'str') -> 'List[str]':
        n = len(s)
        res = []
        for i in range(n - 1):
            if s[i:i+2] == '++':
                res.append(s[:i] + '--' + s[i+2:])
        return res