# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

Let's assume we have n points from 0 to n-1. If we take out three points: (0, k, n-1) 
as the triangle, then we will leave with two polygon: (0 -> k), (k -> n-1).
Therefore, the problem can be solved using DP.

Let dp[i][j] be the minimum score for A[i:j+1].
Then dp[i][j] = min(dp[i][k] + dp[k][j] + A[i] * A[k] * A[j])

Time complexity: O(n^3)
"""
class Solution:
    def minScoreTriangulation(self, A) -> int:
        self.memo = {}
        
        def helper(i, j):
            if j < i + 2:
                self.memo[(i, j)] = 0
            if (i, j) not in self.memo:
                val = float('inf')
                for k in range(i+1, j):
                    val = min(val, helper(i, k) + helper(k, j) + A[i] * A[j] * A[k])
                self.memo[(i, j)] = val
            return self.memo[(i, j)]
        
        return helper(0, len(A) - 1)