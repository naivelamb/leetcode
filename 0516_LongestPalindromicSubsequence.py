# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-palindromic-subsequence/

Standard DP. 
Let dp[i][j] be the length of longest palindromic subsequence for s[i: j + 1].
Hence, dp[i][i] = 1. 
If s[i] == s[j], then dp[i][j] = 2 + dp[i+1][j-1]
else, dp[i][j] = max(dp[i+1][j], dp[i][j-1])

At last, return dp[0][n-1]

Time complexity: O(n^2)
Space complexity: O(n^2)
"""
class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        if s == s[::-1]:
            return n
        
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]