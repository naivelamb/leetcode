"""
https://leetcode.com/problems/search-insert-position/
"""
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        l, r = 0, len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                if nums[mid-1] < target:
                    return mid
                else:
                    r = mid
