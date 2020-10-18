"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

DP1[i][k] => maximum profit of prices[:i+1] with at most k transactions,
(i) dp[i][k] = 0 if i <= 0 or k <= 0
(ii) dp[i][k] = max(dp[i-1][k], prices[i] - prices[j] + dp[j-1][k-1] for j in range(0, i-1))

We can use another dp to get local_max = -prices[j] + dp[j-1][k-1] for j from 0 to i-1

Time complexity: O(nk)
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0
        
        if k >= n // 2: # we can trade as many as possible
            max_profit = 0
            for i in range(1, n):
                max_profit += max(0, prices[i] - prices[i-1])
            return max_profit
        
        dp = [[0] * (k+1) for _ in range(n)]
        for j in range(1, k+1):
            local_max = -prices[0]
            for i in range(1, n):
                dp[i][j] = max(dp[i-1][j], prices[i] + local_max)
                local_max = max(local_max, dp[i-1][j-1] - prices[i]) 
        return dp[-1][k]