"""
https://leetcode.com/problems/unique-paths/
DP[i][j]: # of unique paths to reach position (i, j)
DP[i][j] = DP[i-1][j] + DP[i][j-1]
Time complexity: O(mn)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            dp[0][i] = 1
        for j in range(n):
            dp[j][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]        
