"""
https://leetcode.com/problems/house-robber-ii/

DP, special treatment for last one.
Hence we have two dp array: dp0 for we don't rob House-0; dp1 for we rob House-0. For both dp arrays, dp[i][0] means the maximum money if we don't rob House-i, dp[i][1] means the maximum money if we rob House-i.

Time complexity: O(N)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp0, dp1 = [[0, 0] for _ in range(n)], [[0, 0] for _ in range(n)]
        dp0[0][1] = nums[0]
        dp1[0][1] = nums[0]
        for i in range(1, n):
            if i == 1:
                dp0[i][0] = 0
                dp0[i][1] = nums[i]
                dp1[i][0] = dp1[i-1][1]
                dp1[i][1] = dp1[i-1][1]
            elif i == n - 1:
                dp0[i][0] = max(dp0[i-1])
                dp0[i][1] = dp0[i-1][0] + nums[i]
                dp1[i] = dp1[i-1]
            else:
                dp0[i][0] = max(dp0[i-1])
                dp0[i][1] = dp0[i-1][0] + nums[i]
                dp1[i][0] = max(dp1[i-1])
                dp1[i][1] = dp1[i-1][0] + nums[i]

        return max(dp0[-1] + dp1[-1])
