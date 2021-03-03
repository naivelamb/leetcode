"""
https://leetcode.com/problems/missing-number/
n = len(nums)
(n + 1) * n/2 - sum(nums)
Time complexIty: O(N)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n + 1) * n // 2 - sum(nums)