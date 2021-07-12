"""
https://leetcode.com/problems/reshape-the-matrix/
"""
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0] * c for _ in range(r)]

        if m * n != r * c:
            return mat

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                new_i = idx // c
                new_j = idx % c
                res[new_i][new_j] = mat[i][j]
        return res