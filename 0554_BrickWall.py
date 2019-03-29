# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/brick-wall/

Compute prefix sum for each row, get the most common one and its count.

Time complexty: O(n), n = total number of elements in the wall
"""
class Solution:
    def leastBricks(self, wall):
        ref, ans = {}, 0
        n = len(wall)
        for row in wall:
            pre_sum = 0
            for width in row[:-1]:
                pre_sum += width
                ref[pre_sum] = ref.get(pre_sum, 0) + 1
                ans = max(ans, ref[pre_sum])
        return n - ans