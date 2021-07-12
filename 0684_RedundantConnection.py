"""
https://leetcode.com/problems/redundant-connection/
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
        if px == py:
            return True
        else:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[px] = py
                self.rank[px] += 1
            return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges) + 1)
        for x, y in edges:
            if dsu.union(x-1, y-1):
                return [x, y]