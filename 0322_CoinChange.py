# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/coin-change/

dp[i] => min # of coins for amount i
dp[i] = min(dp[i-c] for all c in coins) + 1
"""
class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = min(dp[i-c] if i - c >= 0 else dp[i] for c in coins) + 1
        return dp[-1] if dp[-1] != float('inf') else -1
