# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Only one trasaction, dp[i] => max profit if sell on day-i
low -> lowest price before day-i
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        dp = len(prices) * [0]
        low = prices[0]
        for i in range(1, len(prices)):
            dp[i] = max(dp[i], prices[i] - low)
            low = min(low, prices[i])
        return max(dp)

p = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(p))