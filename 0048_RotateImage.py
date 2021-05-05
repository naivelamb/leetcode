"""
https://leetcode.com/problems/rotate-image/
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n <= 1:
            return
        
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
        return 