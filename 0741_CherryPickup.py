"""
https://leetcode.com/problems/cherry-pickup/

It is easy if we only need to from start to end.
DP[i, j] -> maximum cherry pickup when we reach the position.
DP[i, j] = maximum(DP[i-1, j], DP[i, j-1]) + grid[i][j] when grid[i][j] != -1.

But it is hard to track the way back, since every path we take changes the grid status in a different manner.

So we can think the problem as two people walking from the start to the end.
DP[r1][c1][c2] be the maximum cherries picked up by the two people when they start from (r1, c1) and (r2, c2) respectively, walking towards (n-1, n-1). r1 + c1 = r2 + c2

DP[r1][c1][c2] = (grid[r1][c1] + grid[r2][c2]) + max(DP[r1+1][c1][c2], DP[r1][c1+1][c2], DP[r1][c1+1][c2+1], DP[r1+1][c1][c2+1])
"""
class Solution:
    def cherryPickup(self, grid) -> int:
        N = len(grid)
        memo = [[[None] * N for _1 in range(N)] for _2 in range(N)]
        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if (N == r1 or N == r2 or N == c1 or N == c2 or grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            elif r1 == c1 == N-1:
                return grid[r1][c1]
            elif memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            else:
                ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                ans += max([dp(r1+1, c1, c2), dp(r1, c1+1, c2), dp(r1, c1+1, c2+1), dp(r1+1, c1,c2+1)])
            memo[r1][c1][c2] = ans
            return ans
        return max(0, dp(0, 0, 0))
