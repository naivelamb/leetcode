# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:01:33 2019

If mid % 2 == 0 and nums[mid] == nums[mid + 1], target is in the right.
Else, target in the left.
If mid % 2 != 0 and nums[mid] == nums[mid - 1], target is in the right.
Else, target in the left.

Binary search.

Time complexity: O(logn)
"""
class Solution:
    def singleNonDuplicate(self, nums):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return nums[r]
