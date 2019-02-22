# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/maximum-gap/

#1 Naive way
Sort then compare neighbors, O(nlogn)
"""
class Solution:
    def maximumGap(self, nums: 'List[int]') -> 'int':
        if len(nums) <= 1:
            return 0
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            ans = max(ans, nums[i] - nums[i - 1])
        return ans
