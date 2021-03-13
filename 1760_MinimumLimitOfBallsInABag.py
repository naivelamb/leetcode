"""
https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

First thought: heap. Always divide the largest bag to 2nd largest bag and another. 
[10^9, 1], ops = 10^9
Time comlexity: O(10^9) ==> TLE

ans[max_ops] >= ans[max_ops + 1]

Give max # of balls k in a bag, check number of ops (sum((x - 1)//k for x in nums)), make sure it <= max_ops

Binary search.

Time complexity: O(nlog(max(nums))), n = len(nums)
"""
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            if sum((x - 1) // mid for x in nums) > maxOperations:
                l = mid + 1
            else:
                r = mid
        return l