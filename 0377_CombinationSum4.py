# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/combination-sum-iv/

#1 DP
dp[i] => number of ways for get i.
dp[i] = sum(dp[i-num] for num in nums)

Time complexity: O(nt), n -> len(nums), t -> target 
"""

class Solution:
    def combinationSum4(self, nums, target):
        nums.sort()
        dp = [0] * (1 + target)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i-num]
        return dp[target]
    
    def combinationSum4_dfs(self, nums, target):
        nums.sort()
        path = []
        combs = []
        self.dfs(nums, target, path, combs)
        return len(combs)
    
    def dfs(self, nums, target, path, combs):
        if target == 0:
            combs.append(path)
        for i in range(0, len(nums)):
            if nums[i] > target:
                break
            self.dfs(nums, target - nums[i], path + [nums[i]], combs)
        