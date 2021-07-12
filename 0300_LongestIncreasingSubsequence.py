"""
https://leetcode.com/problems/longest-increasing-subsequence/

DP[i] => longest increasing subsequence ending with nums[i]
DP[i] = 1 + (max(dp[k] for k in range(i) if nums[k] < nums[i]))

Time complexity: O(n^2)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n + 1)
        res = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            res = max(res, dp[i])
        return res