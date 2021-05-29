"""
https://leetcode.com/problems/maximum-erasure-value/

sliding window. 
Main a sliding window such that every element is unique. When a non-unique element is added, shrink the window from left until the same element is removed. 
Time complexity: O(N)
"""
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = float('-inf')
        curr = 0
        seen = set()
        i = 0
        for j in range(len(nums)):
            while nums[j] in seen:
                curr -= nums[i]
                seen.remove(nums[i])
                i += 1
            seen.add(nums[j])
            curr += nums[j]
            ans = max(ans, curr)
        return ans