"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

4 states: buy, sell, empty, hold. 
buy -> hold
sell -> empty
buy can only come from empty
sell can only come from hold

So states -> own/don't own.

2xn DP. 
DP[0][i] => maximum profit when don't own stock on day-i
DP[1][i] => maximum profit when own stock on day-i.

DP[0][i] = max(DP[0][i-1], DP[1][i-1] + prices[i] - fee)
DP[1][i] = max(DP[1][i-1], DP[0][i-1] - prices[i] - fee)

Time complexity: O(N)
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[-float('inf') for _ in range(n)] for _ in range(2)]
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + prices[i] - fee)
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] - prices[i])
        return max(dp[0][-1], dp[1][-1])