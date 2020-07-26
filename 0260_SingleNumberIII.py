"""
https://leetcode.com/problems/single-number-iii/
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        once, twice = set(), set()
        for n in nums:
            if n in once:
                once.remove(n)
                twice.add(n)
            else:
                once.add(n)
        return list(once)
