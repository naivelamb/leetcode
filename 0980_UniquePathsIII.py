# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/unique-paths-iii/

DFS find all possible paths from start to end, avoiding all obstacles and 
repeatation. Only save those with length == total sites - # of obstacles.
"""
class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        obstacles = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] == -1:
                    obstacles.add((i, j))
        
        target_steps = m*n - len(obstacles)
        def dfs(i, j, path):
            if (i, j) == end:
                if len(path) == target_steps:
                    ans.append(path)
            for di, dj in dirs:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n:
                    if (new_i, new_j) not in path and (new_i, new_j) not in obstacles:
                        dfs(new_i, new_j, path + [(new_i, new_j)])
        
        ans = []
        dfs(start[0], start[1], [start])
        return len(ans)