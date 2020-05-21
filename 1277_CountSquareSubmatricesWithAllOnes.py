"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

DP. Let dp[i][j] be the number of square submatrices if using (i, j) as lower right corner.
If matrix[i][j] == 1, dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1, j-1])
Then we just need to sum dp matrix.

Time complexity: O(mn)
"""
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                ans += dp[i][j]
        return ans
