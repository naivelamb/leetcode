# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/two-sum/

Use hashmap, O(n)
"""
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        if len(nums) <= 1:
            return []
        ref = {}
        for i, n in enumerate(nums):
            if target - n in ref:
                return [ref[target - n], i]
            else:
                ref[n] = i
        return []
    
nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))
