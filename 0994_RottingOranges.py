# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/rotting-oranges/

BFS starting from multiple points simultaneously.
"""

import collections
class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        fresh = set()
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: #fresh
                    fresh.add((i, j))
                if grid[i][j] == 2: #rotten
                    queue.append((i, j, 0))
        
        res = 0
        if not fresh:
            return res
        
        while queue:
            i, j, t = queue.popleft()
            res = max(res, t)
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) in fresh:
                    queue.append((x, y, t + 1))
                    fresh.remove((x, y))
        
        if fresh:
            return -1
        return res
                    
        