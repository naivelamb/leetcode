"""
https://leetcode.com/problems/graph-connectivity-with-threshold/

Build the union-find for all n, based on multilication. Then check the queries. 

Time complexity: O(n^2 + qn)
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
    def areConnected(self, n: int, g: int, queries: List[List[int]]) -> List[bool]:
        if g == 0:
            return [True] * len(queries)
        if g >= n:
            return [False] * len(queries)
        
        dsu = DSU(n)

        for candidate in range(g+1, n+1):
            current = [t * candidate for t in range(1, n//candidate + 1)]
            for curr in current:
                dsu.union(curr-1, candidate-1)
        
        res = []
        for a, b in queries:
            if a > g and b > g and dsu.find(a-1) == dsu.find(b-1):
                res.append(True)
            else:
                res.append(False)
        return res