# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

dp[i][j] => maximum profit for i-th day if:
Hold on i-th day (j = 0)
Sell on i-th day (j = 1)
Empty on i-th day (j = 2)

Findings: 
	1. If we want to sell on day-i, then we must be on 'hold' state on day (i-1)
	2. If we are on 'hold' state on day-i, then we must be on 'empty' or 'hold' 
      state on day (i-1)
   3. If we are on 'empty' state on day-i, then we must be on 'sell' or 'empty'
      state on day (i-1)

Therefore, the dp functions are:
dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i]).
dp[i][1] = dp[i-1][0] + prices[i]
dp[i][2] = max(dp[i-1][1], dp[i-1][2])

Time Complexity: O(n), Space Complexity: O(n)

It can be easily turned to a Time O(n), Space O(1) solution
"""
class Solution:
    def maxProfit_space(self, prices: 'List[int]') -> 'int':
        # Space O(n)
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[-1])
    
    def maxProfit(self, prices: 'List[int]') -> 'int':
        # Space O(1)
        if not prices:
            return 0
        n = len(prices)
        hold, sold, empty = -prices[0], 0, 0
        for i in range(1, n):
            hold, sold, empty = max(hold, empty - prices[i]), hold + prices[i], max(sold, empty)
        return max(hold, sold, empty)

s = Solution()
a = []
print(s.maxProfit(a))
a = [1,2,3,0,2]
print(s.maxProfit(a))