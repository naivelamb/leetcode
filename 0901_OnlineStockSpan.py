"""
https://leetcode.com/problems/online-stock-span/
If we know a price and its span, let's assume the price index is k. Then in the time series array, the elements of prices[k-span:k-1] is useless. 
"""
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
