# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/partition-array-for-maximum-sum/

A number can only influence the K neighbors at most. 
Let dp[i] be the maximum sum for array A[:i+1] with subarrays of length at 
most k.
Then dp[i] = max(dp[i], dp[i-(j+1)] + max(A[i-j:i+1]) * (j+1) for j in range(k))
The max(A[i-j: i+1]) can be computed first. 

Time complexity: O(nk)
"""
class Solution:
    def maxSumAfterPartitioning(self, A, K):
        n, dp = len(A), [0]
        for i in range(n):
            MAX = A[i]
            dp.append(dp[-1] + MAX)
            for j in range(i - 1, max(i-K, -1), -1):
                MAX = max(MAX, A[j])
                dp[-1] = max(dp[-1], dp[j] + MAX * (i - j + 1))
        return dp[-1]
