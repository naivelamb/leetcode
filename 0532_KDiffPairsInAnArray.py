"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/

Get Counter information for nums, then check each number.

Time complexity: O(2N)
"""
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = collections.Counter(nums)
        ans = 0
        for n in nums:
            if n+k in nums:
                if k > 0:
                    ans += 1
                elif nums[n+k] > 1:
                    ans += 1
        return ans
