"""
https://leetcode.com/problems/maximal-square/

dp[i][j] -> largest square edge length using (i, j) as lower-right corner
row[i][j] -> longest # of consecutive 1s for matrix[:i][:] ending at (i, j)
col[i][j] -> longest # of consecutive 1s for matrix[:][:j] ending at (i, j)
if matrix[i][j] == 0 -> dp[i][j] = 0
if matrix[i][j] == 1 -> dp[i][j] = min(dp[i-1][j-1] + 1, row[i][j], col[i][j])

time complexity: O(mn)

"""
class Solution:
    def maximalSquare(self, matrix):

        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        row = [[0] * n for _ in range(m)]
        col = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if j != 0:
                        row[i][j] = row[i][j-1] + 1
                    else:
                        row[i][j] = 1

        for j in range(n):
            for i in range(m):
                if matrix[i][j] == '1':
                    if i != 0:
                        col[i][j] = col[i-1][j] + 1
                    else:
                        col[i][j] = 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1] + 1, row[i][j], col[i][j])
                ans = max(ans, dp[i][j])
        return ans ** 2
