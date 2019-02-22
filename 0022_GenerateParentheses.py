# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/generate-parentheses/

DFS + Memorization
f(n) => parenthesis for n
f(n) = '({}){}'.format(f(a), f(b)) for all a + b == n - 1
"""
import collections
class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if n == 0:
            return ['']
        memo = collections.defaultdict(set)
        memo[0].add('')
        memo[1].add('()')
        def dfs(n):
            if n in memo:
                return memo[n]
            for a in range(0, n):
                for p1 in dfs(a):
                    for p2 in dfs(n - a - 1):
                        memo[n].add('(' + p1 + ')' + p2)
            return memo[n]
        
        return list(dfs(n))
    
    def generateParenthesis_opt(self, n: 'int') -> 'List[str]':
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis_opt(c):
                for right in self.generateParenthesis_backtrack(n - c - 1):
                    ans.append('({}){}'.format(left, right))
        return ans
    
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

s = Solution()
n = 3
print(s.generateParenthesis_opt(3))