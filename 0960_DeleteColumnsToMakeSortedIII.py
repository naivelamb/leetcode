# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

Find maximum increasing subsequence for all strings.
DP[i] => longest increasing subsequence ending with i-th element

Time Complexity: O(m*n^2)
"""

class Solution:
    def minDeletionSize(self, A: 'List[str]') -> 'int':
        m, n = len(A), len(A[0])
        dp = [1] * n
        for j in range(1, n):
            for i in range(j):
                if all(A[k][i] <= A[k][j] for k in range(m)):
                    dp[j] = max(dp[j], dp[i] + 1)
        return n - max(dp)