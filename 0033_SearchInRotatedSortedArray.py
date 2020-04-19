"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

sol = Solution()
assert sol.search([4,5,6,7,0,1,2], 0) == 4
assert sol.search([4,5,6,7,0,1,2], 3) == -1
