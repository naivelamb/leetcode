"""
https://leetcode.com/problems/largest-divisible-subset/

Let's sort the nums first.
If S_i % S_j == 0, S_j % S_k == 0, then S_i % S_k == 0.
dp[i] => largest divisible subset for nums[:i+1].
If nums[j] % nums[i], then dp[j] = dp[i] + nums[j]

Time complexity: O(N^2), N = len(nums)
Space compleixy: O(N^2), N = len(nums)
"""
class Solution:
    def largestDivisibleSubset(self, nums):
        if len(nums) == 0:
            return []
        nums.sort()
        dp = [[num] for num in nums]
        ans = [nums[0]]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(ans):
                ans = dp[i]
        return ans
