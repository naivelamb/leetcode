"""
https://leetcode.com/problems/special-positions-in-a-binary-matrix/

Get row and col non zero count, then go through each postiion.

Time Complexity: O(mn)
"""
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        cnt_row, cnt_col = {}, {}
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    cnt_row[i] = cnt_row.get(i, 0) + 1
                    cnt_col[j] = cnt_col.get(j, 0) + 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and cnt_row[i] == 1 and cnt_col[j] == 1:
                    ans += 1
        return ans
