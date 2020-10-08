"""
https://leetcode.com/problems/binary-search/
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > target or target > nums[-1]:
            return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
