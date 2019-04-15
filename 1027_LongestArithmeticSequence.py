# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-arithmetic-sequence/

DP, dp[i, d] means the length of the arithmetic subsequence ending with A[i] of
difference d. 

Time complexity: O(n^2)
"""
class Solution:
    def longestArithSeqLength(self, A):
        dp = {}
        d = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                d = A[j] - A[i]
                if (i, d) in dp:
                    dp[(j, d)] = dp[(i, d)] + 1
                else:
                    dp[(j, d)] = 1
        return 1 + max(dp.values())