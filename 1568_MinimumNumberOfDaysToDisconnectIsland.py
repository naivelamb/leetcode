"""
https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

We can disconnect island in at most 2 days, as long as we find the corner and cut the nearby islands.

Day-0: count islands, return 0 if less than or more than 1 island, O(mn)
Day-1: try to remove any possible island and count island, return 1 if we get less than or greater than one island, O(m^2n^2)
Day-2: return 2

Overall time complexity: O(mn)
"""

import copy
class Solution:
    def NumIsland(self, grid):
        def dfs(i, j, m, n):
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 0
                    dfs(x, y, m, n)
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    cnt += 1
                    dfs(i, j, m, n)
        return cnt

    def minDays(self, grid: List[List[int]]) -> int:
        ans = 0
        grid_copy = copy.deepcopy(grid)
        n = self.NumIsland(grid_copy)
        if n != 1:
            return ans

        # try to remove
        ans = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid_copy = copy.deepcopy(grid)
                    grid_copy[i][j] = 0
                    n = self.NumIsland(grid_copy)
                    if n != 1:
                        return ans

        return 2
