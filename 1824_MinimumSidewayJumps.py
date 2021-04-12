"""
https://leetcode.com/problems/minimum-sideway-jumps/

DP. 
Time Complexity: O(n)
"""
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles) - 1
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0] = [1, 0, 1]
        for i in range(1, n):
            for r in range(3):
                if obstacles[i] == r + 1 or obstacles[i+1] == r + 1:
                    dp[i][r] = float('inf')
                else:
                    dp[i][r] = min([
                        dp[i-1][r],
                        dp[i-1][(r+1)%3] + 1,
                        dp[i-1][(r+2)%3] + 1,
                    ])
        return min(dp[-1])