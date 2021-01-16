"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

Heap the nums, then pop k. 
Time complexity: N + KlogN
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        res = 0
        for _ in range(k):
            res = heapq.heappop(heap)
        return -res