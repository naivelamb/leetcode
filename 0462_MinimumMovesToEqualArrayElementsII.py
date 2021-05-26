"""
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

The target value is median. Sort then compute.

Time complexity: O(nlogn)
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        mid = n // 2
        nums.sort()
        res = 0
        for i in range(n):
            res += abs(nums[i] - nums[mid])
        return res