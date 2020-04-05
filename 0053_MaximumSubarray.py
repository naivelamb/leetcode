"""
https://leetcode.com/problems/maximum-subarray/
"""
class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0
        pre_sum, ans = nums[0], nums[0]
        for n in nums[1:]:
            pre_sum = max(n, n+pre_sum)
            ans = max(ans, pre_sum)
        return ans
