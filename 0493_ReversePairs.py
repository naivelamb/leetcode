# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/reverse-pairs/

If the list can be divided into two halves, A + B, where A and B are both sorted, 
then we can easily know the important reverse pairs in B for all number in A. 

Therefore, this problem can be solved by a modified merge sort. 

Time complexity: O(nlogn)
"""
class Solution:
    def reversePairs(self, nums):
        if not nums:
            return 0
        return self.merge_and_count(nums, 0, len(nums) - 1)
        
        
    def merge_and_count(self, nums, start, end):
        if start == end:
            return 0
        
        count = 0
        mid = (start + end) // 2
        count += self.merge_and_count(nums, start, mid)
        count += self.merge_and_count(nums, mid + 1, end)
        
        left, right = start, mid + 1
        while left <= mid and right <= end:
            if nums[left] > 2 * nums[right]:
                count += mid - left + 1
                right += 1
            else:
                left += 1
        nums[start: end + 1] = sorted(nums[start: end + 1])
        return count