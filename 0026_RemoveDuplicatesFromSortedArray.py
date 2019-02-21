# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Two pointer
"""
class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) <= 1:
            return len(nums)
        l, r = 0, 1
        while r < len(nums):
            if nums[r] != nums[l]:
                nums[l + 1] = nums[r]
                l += 1
            r += 1
        print(nums)
        return l + 1
    
s = Solution()
n = [1, 1, 2]
print(s.removeDuplicates(n))
n = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(s.removeDuplicates(n))