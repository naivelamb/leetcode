"""
https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

dp[i][j] => minimum time to arrive i-th road with j skips.

Time complexity: O(n^2) 
"""
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        eps = 1e-9
        
        n = len(dist)
        dp = [[10**10 for _ in range(n+1)] for _ in range(n+1)]
        dp[0][0] = 0
        
        for i, d in enumerate(dist, 1):
            dp[i][0] = math.ceil(dp[i-1][0] + d/speed - eps)
            for j in range(1, i + 1):
                dp[i][j] = min(dp[i-1][j-1] + d/speed, math.ceil(dp[i-1][j] + d/speed - eps))
        
        for j, t in enumerate(dp[-1]):
            if t <= hoursBefore:
                return j
        return -1