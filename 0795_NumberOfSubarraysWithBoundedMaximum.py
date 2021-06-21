"""
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

For an abritray number, it must be
1) x < left => can be added to an adjacent subarray to form a new one.
2) left <= x <= right => can be added, can be distinct.
3) x > right => break existing subarray

So we need to record the following things:
prev : previous "break" point
dp : length of previous satisfied subarray. 

For situation (1), it can be added so res += dp
For situation (2), clear dp = 0 and prev = i
For situation (3), dp = i - prev and res += dp

Time complexity: O(N)
"""
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res, dp = 0, 0
        prev = -1
        for i in range(len(nums)):
            if nums[i] < left and i > 0:
                res += dp
            if nums[i] > right:
                prev = i
                dp = 0
            if left <= nums[i] <= right:
                dp = i - prev
                res += dp
        return res