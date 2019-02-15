# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-path-sum/

dp[i][j] => minimum path sum for reach (i, j)
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

Time Complexity: O(mn), Space: O(mn)
"""
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i >= 1 and j >= 1:
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                else:
                    if i >= 1:
                        dp[i][j] = grid[i][j] + dp[i-1][j]
                    if j >= 1:
                        dp[i][j] = grid[i][j] + dp[i][j-1]
        return dp[-1][-1]