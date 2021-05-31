"""
https://leetcode.com/problems/minimum-cost-to-connect-sticks/

if we have n sticks, we need to n-1 combines. We want to combine short ones first. 

heap.

Time complexity: O(nlogn)
"""
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        ans = 0
        heapq.heapify(sticks)
        while len(sticks) >= 2:
            a1 = heapq.heappop(sticks)
            a2 = heapq.heappop(sticks)
            ans += a1 + a2
            heapq.heappush(sticks, a1 + a2)
        return ans