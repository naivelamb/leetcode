"""
https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

Greedy. 
It's always to pick the left most subarray and move forward.

Time complexity: O(mn)

"""
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        for grp in groups:
            for ii in range(i, len(nums)):
                if nums[ii: ii + len(grp)] == grp:
                    i = ii + len(grp)
                    break
            else:
                return False
        return True