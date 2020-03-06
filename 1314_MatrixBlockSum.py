"""
https://leetcode.com/problems/matrix-block-sum/
dp[i][j] is the prefix sum of the matrix

for a given (i, j) and K, we need to find
r1 = max(0, i-K) + 1
r2 = min(m-1, i+K) + 1
c1 = max(0, j-K) + 1
c2 = min(n-1, j+K) + 1

ans[i][j] = dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1]

Time complexity: O(mn)
"""
class Solution:
    def matrixBlockSum(self, mat, K: int):
        m, n = len(mat), len(mat[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] + mat[i-1][j-1] - dp[i-1][j-1]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(0, i-K) + 1
                r2 = min(m-1, i+K) + 1
                c1 = max(0, j-K) + 1
                c2 = min(n-1, j+K) + 1
                ans[i][j] = dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1]

        return ans
