"""
https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

Union-Find.
First union type 3, count if the connection is not necessary.

Then union type 1 and 2 respectively, count if the connection is not necessary.

Finally check whether both UF have only one union.

Time Complexity: O(N)
"""
class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[u] > self.rank[v]:
            self.parents[pv] = pu
        elif self.rank[u] < self.rank[v]:
            self.parents[pu] = pv
        else:
            self.parents[pu] = pv
            self.rank[pv] += 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        dsu1, dsu2 = DSU(n), DSU(n)
        ans = 0
        for t, u, v in edges:
            if t != 3:
                continue
            if not dsu1.union(u-1, v-1) or not dsu2.union(u-1, v-1):
                ans += 1

        for t, u, v in edges:
            if t == 1 and not dsu1.union(u-1, v-1):
                ans += 1
            if t == 2 and not dsu2.union(u-1, v-1):
                ans += 1

        # count number of unions
        r1 = dsu1.find(0)
        r2 = dsu2.find(0)
        for i in range(1, n):
            if dsu1.find(i) != r1 or dsu2.find(i) != r2:
                return -1

        return ans
