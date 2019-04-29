# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/coloring-a-border/

The key is to find the border, use BFS.

Time complexity: O(mn)
"""
import collections
class Solution:
    def colorBorder(self, grid, r0, c0, color):
        m, n = len(grid), len(grid[0])
        ref_color = grid[r0][c0]
        border = []
        queue = collections.deque([(r0, c0)])
        visited = {(r0, c0)}
        while queue:
            x, y = queue.popleft()
            nei = []
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n:
                    nei.append((new_x, new_y))
            cnt = 0
            for a, b in nei:
                if grid[a][b] == ref_color: # same component
                    cnt += 1
                    if (a, b) not in visited:
                        visited.add((a, b))
                        queue.append((a, b))
            
            if cnt != 4: # (x, y) is border
                border.append((x, y))
        
        for x, y in border:
            grid[x][y] = color
        return grid
