"""
https://leetcode.com/problems/longest-consecutive-sequence/

Store all nums to a set. (O(n))
For a number x, if we cannot find (x-1) in the set, we find the head, then we keep increasing it by +1 until we cannot find next available element. 

Overall O(N)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        all_nums = set(nums)
        ans = 0
        for x in nums:
            if x - 1 not in all_nums:
                tmp = 0
                y = x
                while y in all_nums:
                    tmp += 1
                    y += 1
                ans = max(ans, tmp)
        return ans