"""
https://leetcode.com/problems/number-of-closed-islands/

Union-find, build the graph first.
Check all the islands with land at the boundary, move the island to 'open-islands'.
Now count the closed islands.

Time complexity: O(mn * alpha(mn)) ~ O(mn), Union-find with path compression & union by rank
"""
class DSU:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1

class Solution:
    def closedIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        dsu = DSU(m*n)
        islands = set()
        open_islands = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    for dx, dy in dirs:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                            dsu.union(i * n + j, x * n + y)

        for i in range(m):
            if grid[i][0] == 0:
                open_islands.add(dsu.find(i * n))
            if grid[i][n-1] == 0:
                open_islands.add(dsu.find(i * n + n - 1))
        for j in range(n):
            if grid[0][j] == 0:
                open_islands.add(dsu.find(j))
            if grid[m-1][j] == 0:
                open_islands.add(dsu.find((m-1) * n + j))

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    island = dsu.find(i * n + j)
                    if island not in open_islands and island not in islands:
                        ans += 1
                        islands.add(island)

        return ans

sol = Solution()

grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]
assert sol.closedIsland(grid) == 2

grid = [[0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]]
assert sol.closedIsland(grid) == 1

grid = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]]
assert sol.closedIsland(grid) == 2

grid = [[1,0,1,1,1,1,0,0,1,0],
        [1,0,1,1,0,0,0,1,1,1],
        [0,1,1,0,0,0,1,0,0,0],
        [1,0,1,1,0,1,0,0,1,0],
        [0,1,1,1,0,1,0,1,0,0],
        [1,0,0,1,0,0,1,0,0,0],
        [1,0,1,1,1,0,0,1,1,0],
        [1,1,0,1,1,0,1,0,1,1],
        [0,0,1,1,1,0,1,0,1,1],
        [1,0,0,1,1,1,1,0,1,1]]
assert sol.closedIsland(grid) == 3
