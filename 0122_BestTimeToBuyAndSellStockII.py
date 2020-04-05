"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Buy dip an sell top.
"""
class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        if not prices:
            return ans
        buy_price, prev_high = prices[0], prices[0]
        for price in prices[1:]:
            if price < prev_high:
                ans += (prev_high - buy_price)
                buy_price, prev_high = price, price
            else:
                prev_high = price
        ans += (prev_high - buy_price)
        return ans

sol = Solution()
assert sol.maxProfit([7,1,5,3,6,4]) == 7
assert sol.maxProfit([1,2,3,4,5]) == 4
assert sol.maxProfit([7,6,4,3,1]) == 0
