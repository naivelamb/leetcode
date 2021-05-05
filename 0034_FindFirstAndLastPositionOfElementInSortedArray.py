"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Binary search

Time complexity: O(logn)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else: #find target
                left, right = self.findLeft(nums, mid, target), self.findRight(nums, mid, target)
                return [left, right]
        return [-1, -1]
    
    def findLeft(self, nums, idx, target):
        l, r = 0, idx
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                r = mid - 1
            else:
                l = mid + 1
    
    def findRight(self, nums, idx, target):
        l, r = idx, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid
                l = mid + 1
            else:
                r = mid - 1