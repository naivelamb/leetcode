# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/strange-printer/

Let dp(i, j) be the answer to print s[i], s[i+1], s[i+2], …, s[j].
If we have a k, such that i < k < j, and s[i] == s[k], then 
dp(i, j) = dp(i, k - 1) + dp(k + 1, j). 
So we can solve the problem by dp + dfs.
"""
class Solution:
    def strangePrinter(self, s: 'str') -> 'int':
        memo = {}
        def dp(i, j):
            if i > j:
                return 0
            if (i, j) not in memo:
                ans = dp(i + 1, j) + 1
                for k in range(i + 1, j + 1):
                    if s[i] == s[k]:
                        ans = min(ans, dp(i, k - 1) + dp(k + 1, j))
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, len(s) - 1)

s = Solution()
print(s.strangePrinter('aaabbb'))
print(s.strangePrinter('aba'))