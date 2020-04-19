# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/number-of-islands-ii/

We need to update the island everytime we enter a query. This can be addressed
by a union-find, union.

When we enter a query, we check its 4 neighbors, if any of them are island, we
need to join them. Each individual island is marked by the parent in dsu, hence,
we first remove all the island markers of the neighbors from the island set, then
add the new island marker after the union operation.

Time comlexity: O(mn + k), k -> number of queries
"""
class DSU:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n

    def find(self, x): #path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y): # union by rank, low -> high
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
    def numIslands2(self, m, n, positions):
        # initialize
        dsu = DSU(m*n)
        board = [[0] * n for _ in range(m)]
        islands = set()
        ans= []
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i, j in positions:
            board[i][j] = 1
            nei_islands = []
            for di, dj in dirs:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and board[x][y] == 1:
                    nei = x * n + y
                    nei_islands.append(nei)
                    if dsu.find(nei) in islands:
                        islands.remove(dsu.find(nei))
            for nei in nei_islands:
                dsu.union(nei, i * n + j)
            islands.add(dsu.find(i * n + j))
            ans.append(len(islands))
        return ans
