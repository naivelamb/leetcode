"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

Union Find. 

Time complexity: O(E)
"""
class DSU:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [x for x in range(n)]
    
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for x, y in edges:
            dsu.union(x, y)
        res = set()
        for i in range(n):
            res.add(dsu.find(i))
        return len(res)