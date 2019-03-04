# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/max-increase-to-keep-city-skyline/

Get the sky lines for row and col. Then the max increase for [i][j] is:
    min(max_row[i], max_col[j]) - grid[i][j]

Time complexity: O(n^2)
"""
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        max_row = []
        for row in grid:
            max_row.append(max(row))
        max_col = []
        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            max_col.append(max(col))
        
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(max_row[i], max_col[j]) - grid[i][j]
        
        return ans

    def maxIncreaseKeepingSkyline_pythonic(self, grid):
        max_row, max_col = list(map(max, grid)), list(map(max, zip(*grid)))
        return sum(min(i, j) for i in max_row for j in max_col) - sum(map(sum, grid))
        
s = Solution()
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(s.maxIncreaseKeepingSkyline(grid))
