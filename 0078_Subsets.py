# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/subsets/

combination for all possible i, i <= n, n = len(nums)
"""
class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        self.res = []
        
        def dfs(d, m, curr, idx):
            if d == m:
                self.res.append(curr[:])
                return
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                dfs(d + 1, m, curr, i + 1)
                curr.pop()
                
        for m in range(len(nums) + 1):
            dfs(0, m, [], 0)
        return self.res
