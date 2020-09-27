"""
https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

Simulation.
Time Comlexity: O(sum(customer)/4)
"""
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        queue_customer = 0
        total_profit = [0]
        for c in customers:
            queue_customer += c
            n_board = min(4, queue_customer)
            queue_customer -= n_board
            total_profit.append(total_profit[-1] + n_board * boardingCost - runningCost)

        while queue_customer > 0:
            n_board = min(4, queue_customer)
            queue_customer -= n_board
            total_profit.append(total_profit[-1] + n_board * boardingCost - runningCost)

        max_profit = max(total_profit)
        if max_profit <= 0:
            return -1
        else:
            for i, p in enumerate(total_profit):
                if p == max_profit:
                    return i
