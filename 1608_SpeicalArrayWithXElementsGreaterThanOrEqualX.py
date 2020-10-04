"""
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

Sort the array, then check each number using binary search.

Time compelxity: O(NlogN)
"""
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(max(nums) + 1):
            idx = bisect.bisect_left(nums, i)
            if n - idx == i:
                return i
        return -1
