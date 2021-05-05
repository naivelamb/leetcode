"""
https://leetcode.com/problems/maximum-ice-cream-bars/

Sort and greedy. 

Time complexity: O(nlogn)
"""
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        ans = 0
        while coins >= 0 and costs:
            if coins >= costs[0]:
                coins -= heapq.heappop(costs)
                ans += 1
            else:
                break
        return ans