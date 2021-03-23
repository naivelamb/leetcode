"""
https://leetcode.com/problems/maximum-ascending-subarray-sum/

Greedy, try to find ascending subarray as long as possible.

Time complexity: O(N)
"""
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += nums[i]
            else:
                ans = max(ans, curr)
                curr = nums[i]
        
        ans = max(ans, curr)
        return ans