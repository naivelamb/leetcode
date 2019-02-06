# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/regions-cut-by-slashes/

Use DSU to solve the problem
Each square is represented by
  \0/
  1|3
  /2\
'\' means union (0, 3) and (1, 2)
'/' means union (0, 1) and (2, 3)
' ' means union all of them. 

Aslo need to union neighbors which are:
up: 0 and 'upper' 2
down: 2 and 'lower' 0
left: 1 and 'left' 3
right: 3 and 'right' 1

At the end, just check how may clusters do we have.

Time Complexity: O(n^2)
"""
class DSU:
    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [0] * N
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.p[py] = px
            elif self.rank[px] < self.rank[py]:
                self.p[px] = py
            else:
                self.p[py] = px
                self.rank[px] += 1
                
    
class Solution:
    def regionsBySlashes(self, grid: 'List[str]') -> 'int':
        n = len(grid)
        dsu = DSU(4*n**2)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r*n + c)
                if val == '/':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                elif val == '\\':
                    dsu.union(root + 0, root + 3)
                    dsu.union(root + 1, root + 2)
                else:
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 1, root + 2)
                    dsu.union(root + 2, root + 3)
                # up/down
                if r + 1 < n:
                    dsu.union(root + 2, (root + 4 * n) + 0)
                if r - 1 >= 0:
                    dsu.union(root + 0, (root - 4 * n) + 2)
                # left/right
                if c + 1 < n:
                    dsu.union(root + 3, (root + 4) + 1)
                if c - 1 >= 0:
                    dsu.union(root + 1, (root - 4) + 3)
        
        return sum(dsu.find(x) == x for x in range(4*n**2))
