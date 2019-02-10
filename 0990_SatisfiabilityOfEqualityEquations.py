# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/satisfiability-of-equality-equations/

Union-find, union all '==', then check'!='
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
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        dsu = DSU(26)
        
        neqs = []
        for eq in equations:
            a, b, op = eq[0], eq[-1], eq[1]
            if op == '=':
                dsu.union(ord(a) - ord('a'), ord(b) - ord('a'))
            else:
                neqs.append(eq)
        
        for eq in neqs:
            a, b = eq[0], eq[-1]
            if dsu.find(ord(a) - ord('a')) == dsu.find(ord(b) - ord('a')):
                return False
        return True

a = ["b==a","a==b"]
b = ["a==b","b!=c","c==a"]
s = Solution()
print(s.equationsPossible(a))
print(s.equationsPossible(b))