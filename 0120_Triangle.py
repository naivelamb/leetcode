"""
https://leetcode.com/problems/triangle/
DP. 
Time compleixty: O(N), N = # of nodes
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[0]
        if len(triangle) == 1:
            return dp[0]
        for vals in triangle[1:]:
            new_dp = vals
            for i in range(len(vals)):
                if i == 0:
                    new_dp[i] += dp[i]
                elif i == len(vals) - 1:
                    new_dp[i] += dp[-1]
                else:
                    new_dp[i] += min(dp[i-1], dp[i])
            dp = new_dp
        return min(dp)