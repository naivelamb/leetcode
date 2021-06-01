"""
https://leetcode.com/problems/paint-house/

dp

time complexity: O(N)
"""
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        for i in range(1, len(costs)):
            pre = dp[:]
            for j in range(3):
                dp[j] = costs[i][j] + min(pre[k] if k != j else float('inf') for k in range(3))
        return min(dp)