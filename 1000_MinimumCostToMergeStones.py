# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-cost-to-merge-stones/

This is a 3D dynamic programming problem. =_=
Let dp[i][j][m] be the minimum cost of merging stones[i] to stones[j] into m 
piles. 
Then, dp[i][j][m] = min(dp[i][mid][1] + dp[mid+1][j][m-1]) for all mid in 
[i, j) in the step of (K - 1). 
And, dp[i][i][1] = 0, dp[i][i][m] = INF

We need to find dp[0][n-1][1].

First, when (N - 1) % (K - 1) != 0, we cannot merge the stones into 1 pile, 
return -1. 

The dp can be solved top-down in a recursive way. 
When m == 1, we need to find the answer is dp(i, j, K) + sum(stones(i, j + 1)). 
Hence, we need the compute prefix sum. 

If (j - i + 1 - m) % (K - 1) != 0, then we cannot reach the target, therefore 
dp(i, j, m) == INF.

Time Complexity: O(n^3/K)

"""
class Solution:
    def mergeStones(self, stones, K):
        N = len(stones)
        if (N - 1) % (K - 1):
            return -1
        
        INF = float('inf')
        memo = {}
        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1] + x)
        
        def dp(i, j, m):
            if (j - i + 1 - m) % (K - 1):
                return INF
            if (i, j, m) in memo:
                return memo[i, j, m]
            if i == j:
                res = 0 if m == 1 else INF
            else:
                if m == 1:
                    res = dp(i, j, K) + prefix[j + 1] - prefix[i]
                else:
                    res = INF
                    for mid in range(i, j, K - 1):
                        res = min(res, dp(i, mid, 1) + dp(mid + 1, j, m - 1))
            memo[i, j, m] = res
            return res
        
        res = dp(0, N - 1, 1)
        return res if res < INF else 0
