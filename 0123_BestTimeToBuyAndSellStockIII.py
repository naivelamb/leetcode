"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Need to find a break-point k, then earch for the best one transaction in prices[:k] and prices[k:] respectively.

Brute force would be O(N^2).

We can use two dp array to avoid duplication.
DP1[i] -> max profit if one transaction before day-i.
DP2[i] -> max profit if buy on day-i
ans = max(DP1[i] + DP2[i] for i in range(n))

Time Complexity: O(N)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp1 = [0] * n # max profit if one transaction before day-i
        min_price = prices[0]
        ans = 0
        for i in range(n):
            min_price = min(prices[i], min_price)
            ans = max(ans, prices[i] - min_price)
            dp1[i] = ans

        dp2 = [0] * n # max profit if buy on day-i
        max_price = prices[-1]
        ans = 0
        for i in range(n-1, -1, -1):
            max_price = max(prices[i], max_price)
            ans = max(ans, max_price - prices[i])
            dp2[i] = ans

        total = 0
        for i in range(n):
            total = max(total, dp1[i] + dp2[i])
        return total
