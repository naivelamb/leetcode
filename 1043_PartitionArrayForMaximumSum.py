# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/partition-array-for-maximum-sum/

A number can only influence the K neighbors at most. 
Let dp[i] be the maximum sum for array A[:i+1] with subarrays of length at 
most k.
Then dp[i] = max(dp[i], dp[i-(j+1)] + max(A[i-j:i+1]) * (j+1) for j in range(k))

Time complexity: O(nk)
"""
class Solution:
    def maxSumAfterPartitioning(self, A, K):
        n = len(A)
        dp = [0] * (n + K)
        
        for i in range(n):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i-k+1])
                dp[i] = max(dp[i], dp[i-k] + curMax*k)
        return dp[n - 1]
