"""
https://leetcode.com/problems/frequency-of-the-most-frequent-element/

Sort the array, then sliding window. 

The window is valid if sum(window) + k >= (j - i + 1) * A[j]

Time complexity: O(nlogn)
"""
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l, total, ans = 0, 0, 0
        nums.sort()
        for r in range(len(nums)):
            if total + k >= (r - l) * nums[r]:
                ans = max(ans, r - l + 1)
            else:
                total -= nums[l]
                l += 1
            total += nums[r]
        return ans