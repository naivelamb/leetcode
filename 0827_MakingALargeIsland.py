"""
https://leetcode.com/problems/making-a-large-island/

1. Check all island, compute the area and index them.
2. Try to change 0 to 1 one-by-one, check the neighbor islands, compute the area.

Time complexity: O(n^2)
"""
class Solution:
    def largestIsland(self, grid) -> int:
        N = len(grid)
        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, index):
            area = 0
            grid[x][y] = index
            for new_x, new_y in move(x, y):
                if grid[new_x][new_y] == 1:
                    area += dfs(new_x, new_y, index)
            return area + 1

        index = 2
        area = {}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    area[index] = dfs(x, y, index)
                    index += 1

        res = max(area.values() or [0])
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible_idx = set()
                    for new_x, new_y in move(x, y):
                        if grid[new_x][new_y] > 1:
                            possible_idx.add(grid[new_x][new_y])
                    res = max(res, sum(area[idx] for idx in possible_idx) + 1)

        return res

sol = Solution()
grid = [[1, 0], [0, 1]]
assert sol.largestIsland(grid) == 3
grid = [[1, 1], [1, 0]]
assert sol.largestIsland(grid) == 4
grid = [[1, 1], [1, 1]]
assert sol.largestIsland(grid) == 4
