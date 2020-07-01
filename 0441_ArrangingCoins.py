"""
https://leetcode.com/problems/arranging-coins/
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        total_coins = 0
        k = 0
        while True:
            k += 1
            if total_coins + k > n:
                return k - 1
            total_coins += k
