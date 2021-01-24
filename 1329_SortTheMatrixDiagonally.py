"""
https://leetcode.com/problems/sort-the-matrix-diagonally/

Traverse diagonlly, store elements into an array, sort it then assign back. 

Time complexity： mnlog(D), D = min(M, N)
"""
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        start_i = 0
        while start_i < m:
            i, j, tmp = start_i, 0, []
            while 0 <= i < m and 0 <= j < n:
                tmp.append(mat[i][j])
                i += 1
                j += 1
            tmp.sort()
            i, j, k = start_i, 0, 0
            while 0 <= i < m and 0 <= j < n:
                mat[i][j] = tmp[k]
                i += 1
                j += 1
                k += 1
            start_i += 1
        start_j = 1
        while start_j < n:
            i, j, tmp = 0, start_j, []
            while 0 <= i < m and 0 <= j < n:
                tmp.append(mat[i][j])
                i += 1
                j += 1
            tmp.sort()
            i, j, k = 0, start_j, 0
            while 0 <= i < m and 0 <= j < n:
                mat[i][j] = tmp[k]
                i += 1
                j += 1
                k += 1
            start_j += 1
        return mat