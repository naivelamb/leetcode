"""
https://leetcode.com/problems/coin-change-2/

dp[i] -> for amount i, # of combinations to make the change.
dp[i] += dp[i-c] for all c in coins

Time complexity: O(NC), N=amount, C=len(coins)
"""
class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amount+1):
                if i - c >= 0:
                    dp[i] += dp[i-c]
        return dp[-1]
