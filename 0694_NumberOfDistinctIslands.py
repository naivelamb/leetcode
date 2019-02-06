# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/number-of-distinct-islands/

Given a starting point (i, j) such that grid[i][j] = 1, the island can be found
by DFS.

The difficulty is finding a method to hash the shape of island. The idea used 
is achoring to the top left point. 
e.g. An island [(0, 0), (0, 1), (1, 1)] is the same as [(2, 2), (2, 3), (3, 3)]
If we minus the top left point for the second island, we have [(0, 0), (0, 1), 
(1, 1 )], which is exactly the same as the first one.

Time Complexity: O(m*n), m = len(grid), n = len(grid[0])
"""

class Solution:
    def numDistinctIslands(self, grid: 'List[List[int]]') -> 'int':
        m, n = len(grid), len(grid[0])
        def dfs(i, j, i0, j0):
            # find all islands connected to (i, j)
            # (i0, j0) top left point
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for di, dj in dirs:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    curr.append((x - i0, y - j0))
                    grid[x][y] = '#'
                    dfs(x, y, i0, j0)
        
        shapes = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    curr = []
                    dfs(i, j, i, j)
                    curr = tuple(curr)
                    shapes.add(curr)
        return len(shapes)