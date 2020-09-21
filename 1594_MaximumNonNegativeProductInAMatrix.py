"""
https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

DP
dp1[i][j]-> maximum product for position (i, j)
dp2[i][j]-> minimum product for position (i, j)

dp1[i][j] = max(grid[i][j]*[dp1[i-1][j], dp1[i][j-1], dp2[i-1][j], dp2[i][j-1]])
dp2[i][j] = min(grid[i][j]*[dp1[i-1][j], dp1[i][j-1], dp2[i-1][j], dp2[i][j-1]])

Time Complexity: O(mn)
"""
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp1, dp2 = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
        dp1[0][0] = grid[0][0]
        dp2[0][0] = grid[0][0]
        # initialize 1st row
        for j in range(1, n):
            dp1[0][j] = max(grid[0][j] * dp1[0][j-1], grid[0][j] * dp2[0][j-1])
            dp2[0][j] = min(grid[0][j] * dp1[0][j-1], grid[0][j] * dp2[0][j-1])
        # initialize 1st col
        for i in range(1, m):
            dp1[i][0] = max(grid[i][0] * dp1[i-1][0], grid[i][0] * dp2[i-1][0])
            dp2[i][0] = min(grid[i][0] * dp1[i-1][0], grid[i][0] * dp2[i-1][0])

        # compute the dp array
        for i in range(1, m):
            for j in range(1, n):
                cands = [dp1[i-1][j], dp1[i][j-1], dp2[i-1][j], dp2[i][j-1]]
                dp1[i][j] = max(grid[i][j] * cand for cand in cands)
                dp2[i][j] = min(grid[i][j] * cand for cand in cands)

        ans = max(dp1[-1][-1], dp2[-1][-1])
        if ans < 0:
            return -1
        else:
            return ans % (10**9 + 7)           
