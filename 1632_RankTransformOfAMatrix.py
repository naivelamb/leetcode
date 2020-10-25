"""
https://leetcode.com/problems/rank-transform-of-a-matrix/

We need to start from assigning the smallest rank. Hence we need to go from small to big. 
So, we need dict where dict[a] stores all (i, j) such that A[i][j] = a.

For a value A, we need to find all the positions that share the same row/col (these positions need to share the same rank). Then, we need to find the maximum rank, and assign (1+rank_max) to these positions. 

Therefore, for a given value A, we need to use union-find to group all the rows/cols that can be linked by this value. 

Time complexity: O(mnlog(mn))
"""
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[matrix[i][j]].append([i, j])
        rank = [0] * (m+n) # current maximum rank for row & col
        ans = [[0] * m for _ in range(n)]

        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]
        
        for a in sorted(d):
            p = list(range(m+n))
            rank2 = rank[:]
            for i, j in d[a]:
                i, j = find(i), find(j+n)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])
            for i, j in d[a]:
                rank[i] = rank[j+n] = ans[i][j] = rank2[find(i)] + 1
        return ans