"""
https://leetcode.com/problems/diagonal-traverse/
"""
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        dirs = [(-1, 1), (1, -1)]
        M, N = len(matrix), len(matrix[0])
        ans = []
        i, j, d = 0, 0, 0
        while i < M and j < N:
            ans.append(matrix[i][j])
            di, dj = dirs[d % 2]
            if i + di < 0:
                if j + dj >= N:
                    di = 1
                    dj = 0
                else:
                    di = 0
                d += 1
            elif i + di >= M:
                di, dj = 0, 1
                d += 1
            elif j + dj < 0 or j + dj >= N:
                di, dj = 1, 0
                d += 1
            i += di
            j += dj
        return ans