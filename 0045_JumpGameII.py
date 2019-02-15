# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/jump-game-ii/submissions/

BFS. From the start, we know the possible landing positions, then we go over 
all of them, until we land at the end. 
We can assume that we can always reach the last index, therefore all nums >= 1
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end, jumps = 0, 0, 0
        while end < len(nums) - 1:
            jumps += 1
            max_end = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= len(nums) - 1:
                    return jumps
                max_end = max(max_end, i + nums[i])
            start, end = end + 1, max_end
        return jumps

s = Solution()
nums = [0]
print(s.jump(nums))
nums = [2,3,1,1,4]
print(s.jump(nums))