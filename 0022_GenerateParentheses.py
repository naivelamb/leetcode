# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/generate-parentheses/

DFS + Memorization
f(n) => parenthesis for n
f(n) = f(a) + f(b) for all a + b == n
plus '(' + f(n-1) + ')'
"""
import collections
class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if n == 0:
            return ['']
        memo = collections.defaultdict(set)
        memo[1].add('()')
        def dfs(n):
            if n in memo:
                return memo[n]
            for a in range(1, n):
                b = n - a
                for p1 in dfs(a):
                    for p2 in dfs(b):
                        memo[n].add(p1 + p2)
            for p in dfs(n - 1):
                memo[n].add('(' + p + ')')
            return memo[n]
        
        return list(dfs(n))

    def generateParenthesis_backtrack(self, n: 'int') -> 'List[str]':
        ans = []
        def dfs(S, left, right):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                dfs(S + '(', left + 1, right)
            if right < left:
                dfs(S + ')', left, right + 1)
        dfs('', 0, 0)
        return ans