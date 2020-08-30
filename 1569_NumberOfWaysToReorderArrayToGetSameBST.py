"""
https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
"""
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def f(nums):
            if len(nums) <= 2:
                return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            return comb(len(left)+len(right), len(right)) * f(left) * f(right)
            
        return (f(nums)-1) % (10**9+7)
