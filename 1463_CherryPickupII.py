"""
https://leetcode.com/problems/cherry-pickup-ii/

DP[i][j1][j2] => maximum cherry if (i, j1), (i, j2) are picked by robots.

To reach DP[i][j1][j2], robots can come from [(i-1, j1-1), (i-1, j1), (i-1, j1+1)] and [(i-1, j2-1), (i-1, j2), (i-1, j2+1)] respectively. If j1 == j2, we need to make sure grid[i][j1] is counted only once. 

To prevent robot from going out, we set the dp as dimension of (M, N+2, N+2), and filled with -float('inf'). Hence it would prevent robot from moving out bound. 

Time complexity: O(mn^2)
"""
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])

        dp = [[[-float('inf')] * (N + 2) for _ in range(N + 2)] for _ in range(M)]
        dp[0][1][N] = grid[0][0] + grid[0][N-1]
        for i in range(1, M):
            for j1 in range(1, N+1):
                for j2 in range(1, N+1):
                    cand_prev = -float('inf')
                    for shift1 in [-1, 0, 1]:
                        for shift2 in [-1, 0, 1]:
                            cand_prev = max(cand_prev, dp[i-1][j1 + shift1][j2 + shift2])
                    dp[i][j1][j2] = (grid[i][j1-1] + grid[i][j2-1]) // (1 + (j1 == j2)) + cand_prev
        return max(list(map(max, *dp[-1])))