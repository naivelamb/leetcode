# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/smallest-range/

Put the first element into a heap, this is our initial range. 
Try to remove smallest from the heap, then we need to put the next element in 
that list back to the heap. 
Keep this process until we used up one of the lists.

Time complexity: O(mlogk), m -> total number in the lists of list, k -> len(nums) 
"""
import heapq
class Solution:
    def smallestRange(self, nums):
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)
        
        ans = (-10**5, 10**5)
        right = max(row[0] for row in nums)
        while True:
            left, i, j = heapq.heappop(heap)
            if right - left < ans[1] - ans[0]:
                ans = (left, right)
            if j + 1 == len(nums[i]):
                return ans
            val = nums[i][j + 1]
            right = max(right, val)
            heapq.heappush(heap, (val, i, j + 1))
        
