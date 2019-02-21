# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/move-zeroes/

Two pointers
1st -> first zero position
2nd -> first non-zero position
swap, 1st + 1
"""
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        
        i = 0
        while i < len(nums) and nums[i] != 0:
            i += 1
        l, r = i, i + 1
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            else:
                r += 1