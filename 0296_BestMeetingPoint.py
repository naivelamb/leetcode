# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/best-meeting-point/

Median minimize the absolute distance of points. So we collect all the 
coordinates of the points, then find the median.

Time complexity: O(mnlog(mn))
"""
class Solution:
    def minTotalDistance(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        xs, ys = [], []
        for x in range(n):
            for y in range(m):
                if grid[y][x] == 1:
                    xs.append(x)
                    ys.append(y)
        xs.sort()
        ys.sort()
        n = len(xs)
        meet_point = [xs[n//2], ys[n//2]]
        res = 0
        for i in range(n):
            res += abs(meet_point[0] - ys[i]) + abs(meet_point[1] - xs[i])
        return res

