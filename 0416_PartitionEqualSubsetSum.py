# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/partition-equal-subset-sum/

#1 DFS
We try to build subset that gives the target (sum(nums) // 2). => DFS 
Sort to avoid duplication. 

#2 DP
dp[i][j] => can nums[:i+1] for subset whose sum is j?
dp[i][j] = dp[i-1][j-nums[i-1]] if j >= nums[i-1]

Time complexity: O(mn), m = sum(target) // 2
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
    
    def canPartition_dp(self, nums):
        total = sum(nums)
        n = len(nums)
        if total % 2: return False
        target = total // 2
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        # dp[i][j]nums[:i+1] can sum to j
        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i-1][j]
                if j - nums[i - 1] >= 0 and dp[i-1][j - nums[i-1]]:
                    dp[i][j] = True
        return dp[n][target] 
                        