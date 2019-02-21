# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/permutations/

DFS + backtracking
"""

class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        used = [0] * len(nums)
        self.res = []
        for i in range(len(nums)):
            used[i] = 1
            self.dfs(nums, [nums[i]], used)
            used[i] = 0
        return self.res
    
    def dfs(self, nums, curr, used):
        if len(curr) == len(nums):
            self.res.append(curr[:])
            return
        
        for i in range(len(nums)):
            if used[i] == 1:
                continue
            used[i] = 1
            self.dfs(nums, curr + [nums[i]], used)
            used[i] = 0

s = Solution()
nums = [1, 2, 3]
print(s.permute(nums))