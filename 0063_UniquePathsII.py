"""
https://leetcode.com/problems/unique-paths-ii/

DP

time complexity: O(mn)
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0: return 0

        for i in range(m):
            for j in range(n):
                if i > 0 or j > 0:
                    if obstacleGrid[i][j] == 1:
                        dp[i][j] = 0
                    else:
                        if i >= 1:
                            dp[i][j] += dp[i-1][j]
                        if j >= 1:
                            dp[i][j] += dp[i][j-1]
                
        return dp[-1][-1]