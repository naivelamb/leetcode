"""
https://leetcode.com/problems/running-sum-of-1d-array/

prefix sum
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        for n in nums[1:]:
            res.append(res[-1] + n)
        return res