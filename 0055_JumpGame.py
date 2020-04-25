"""
https://leetcode.com/problems/jump-game/

dp[i], the max index one can reach from [0, i].
dp[i] = max(dp[i-1], i+nums[i])
Return True if dp[-1] >= len(nums) - 1
"""
class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) < 2:
            return True
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] < i:
                return False
            dp[i] = max(dp[i-1], i+nums[i])
        return dp[i-1] >= len(nums) - 1
