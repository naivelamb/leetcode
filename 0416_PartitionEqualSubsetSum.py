# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/partition-equal-subset-sum/

We try to build subset that gives the target (sum(nums) // 2). => DFS 
Sort to avoid duplication. 

Time complexity:
"""
class Solution:
    def canPartition(self, nums):
        nums.sort()
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        
        def dfs(idx, target):
            #Can we form a subset starting from idx, gives sum == target?
            if target == 0:
                return True
            for i in range(idx, len(nums)):
                if i != idx and nums[i] == nums[i-1]:
                    continue
                if nums[i] > target:
                    break
                if dfs(i + 1, target - nums[i]):
                    return True
            return False
        
        return dfs(0, target)