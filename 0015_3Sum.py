# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/3sum/

#1 use hashmap, O(n^2)
#2 Based on two sum. 
"""
import collections
class Solution:
    def threeSum_dict(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        if n < 3:
            return []
        res = set()
        ref = collections.defaultdict(list)
        for i, x in enumerate(nums):
            ref[x].append(i)
        
        for i in range(n):
            for j in range(i + 1, n):
                target = -nums[i] - nums[j]
                if ref[target] and ref[target][-1] > j:
                    res.add((nums[i], nums[j], target))
        
        return [list(x) for x in res]
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """    
        n = len(nums)
        if n < 3: return []
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            tmp = self.twoSum(nums[i+1: ], -nums[i])
            res += tmp
        return res
    
    def twoSum(self, nums, target):
        l, r = 0, len(nums) - 1
        ans = []
        while l < r:
            if nums[l] + nums[r] == target:
                ans.append([-target, nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return ans