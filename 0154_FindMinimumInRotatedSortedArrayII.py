"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Binary search to find the pivot point, then get the minimum value.

Time Complexity: O(logN)
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r = r - 1
        return nums[l]
