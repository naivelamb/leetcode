"""
https://leetcode.com/problems/minimum-distance-to-the-target-element/

go left & right from start.

Time complexity: O(N)
"""
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        l = r = start
        while l >= 0 or r < n:
            if l >= 0 and nums[l] == target:
                return abs(l - start)
            if r < n and nums[r] == target:
                return abs(r - start)
            l -= 1
            r += 1
                