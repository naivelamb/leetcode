"""
https://leetcode.com/problems/number-of-orders-in-the-backlog/

Two pq. 
buy is a max-heap, sell is a min-heap. 

Time complexity:
O(NlogN)
"""
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell_back = []
        buy_back = []
        for price, amount, o_type in orders:
            if o_type == 0:
                if not sell_back or sell_back[0][0] > price:
                    # no excute
                    heapq.heappush(buy_back, (-price, amount))
                else:
                    # excute
                    while sell_back and sell_back[0][0] <= price and amount > 0:
                        s_price, s_amount = heapq.heappop(sell_back)
                        if s_amount < amount:
                            amount -= s_amount
                        else:
                            heapq.heappush(sell_back, (s_price, s_amount - amount))
                            amount = 0
                    if amount > 0:
                        heapq.heappush(buy_back, (-price, amount))
                
            else:
                if not buy_back or -buy_back[0][0] < price:
                    # no excute
                    heapq.heappush(sell_back, (price, amount))
                else:
                    # excute
                    while buy_back and -buy_back[0][0] >= price and amount > 0:
                        b_price, b_amount = heapq.heappop(buy_back)
                        if b_amount < amount:
                            amount -= b_amount
                        else:
                            heapq.heappush(buy_back, (b_price, b_amount - amount))
                            amount = 0
                    if amount > 0:
                        heapq.heappush(sell_back, (price, amount))
            
        ans = 0
        for _, n in (sell_back + buy_back):
            ans += n
        return ans%(10**9 +7)