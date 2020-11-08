"""
https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

Simulation & greedy. Always sell from the balls with most inventory, we try to sell to next inventory, and it's easy to calculate the profit. 

Time compleixty: O(nlogn)
"""

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        ans = 0
        cnt = collections.defaultdict(int)
        cnt[0] = 0
        for n in inventory:
            cnt[n] += 1
        vals = sorted(cnt.keys())[::-1]

        for i, v in enumerate(vals):
            if orders == 0:
                return ans % (10**9 + 7)
                
            v_next = vals[i+1]
            max_orders = (v - v_next) * cnt[v]
            if orders >= max_orders:
                ans += (v + v_next + 1) * (v - v_next) * cnt[v] // 2
                orders -= max_orders
                cnt[v_next] += cnt[v]
            else:
                k = orders // cnt[v]
                remain = orders - k * cnt[v]
                ans += (v + v - k + 1) * k * cnt[v] // 2
                ans += (v - k) * remain
                orders = 0
        return ans % (10**9 + 7)



