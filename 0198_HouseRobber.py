# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/house-robber/

dp[i] => maxProfit if rob house i
dp[i] = max(dp[i - 2] + nums[i], dp[i - 3] + nums[i])
"""
class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]
        ans = max(dp[0], dp[1], dp[2])
        for i in range(3, len(nums)):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
            ans = max(ans, dp[i])
        return ans
