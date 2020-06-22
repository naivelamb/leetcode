"""
https://leetcode.com/problems/single-number-ii/

Ans = (sum(unique)*3 - sum(all_numbers))/2
"""
class Solution:
    def singleNumber(self, nums) -> int:
        seen = set()
        for n in nums:
            seen.add(n)
        return int((sum(seen)*3 - sum(nums))/2)
