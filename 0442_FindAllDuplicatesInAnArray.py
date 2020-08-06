"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/

All a[i] in range [1, n], so if a num is duplicated, then we have two pointers pointing to the same number.
While we go through the list, we put the pointed number to be negative. If we see another pointer pointing to a negative number, it means this pointer has appeared onse, put it in the answer candidates.

Time Complexity: O(N). Space Complexity: O(1)
"""
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i])] *= -1
            else:
                ans.append(abs(nums[i]))
        return ans
