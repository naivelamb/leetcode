"""
https://leetcode.com/problems/number-of-islands/

1). Union Find.
Time complexity: O(MN)
2). DFS
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
    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dsu = DSU(m*n)
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for d in dirs:
                        nr, nc = i + d[0], j + d[1]
                        if (0 <= nr < m) and (0 <= nc < n) and grid[nr][nc] == '1':
                            dsu.union(i*n+j, nr*n+nc)
        ans = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans.append(dsu.find(i*n+j))
        cnt = len(set(ans))

        return cnt

    def numIslands_dfs(self, grid) -> int:
        def dfs(grid, i, j):
            m, n = len(grid), len(grid[0])
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    cnt += 1
        return cnt
sol = Solution()
