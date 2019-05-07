# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/valid-boomerang/

Check if slopes equal to each other
Time complexity: O(1)
"""

class Solution:
    def isBoomerang(self, points) -> bool:
        p1, p2, p3 = points
        return (p1[0] - p2[0]) * (p1[1] - p3[1]) != (p1[0] - p3[0]) * (p1[1] - p2[1])