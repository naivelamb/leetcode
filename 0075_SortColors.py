# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/sort-colors/

l -> index of 0, -1
r -> index 0f 2, len(nums)
scan from the begining, i = 0
if nums[i] = 2, r -= 1, nums[i], nums[r] = nums[r], nums[i]
if nums[i] = 1, i += 1
if nums[i] = 0, l += 1, nums[i], nums[l] = nums[l], nums[i]
"""
class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        l, i, r = -1, 0, len(nums)
        while i < r:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                r -= 1
                nums[i], nums[r] = nums[r], nums[i]
            else:
                l += 1
                nums[l], nums[i] = nums[i], nums[l]
                i += 1