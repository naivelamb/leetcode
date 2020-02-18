"""
https://leetcode.com/problems/largest-1-bordered-square/

For each position, we need to find how many consecutive 1s are on top & left of it (O(N^2)).
Then for each position, we need to find the diagonal position, that furthest away from it to build the largest square subgrid.

Time complexity: O(N^3)
"""

class Solution:
    def largest1BorderedSquare(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        top, left, bottom, right = [a[:] for a in grid], [a[:] for a in grid], [a[:] for a in grid], [a[:] for a in grid]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i:
                        top[i][j] = top[i-1][j] + 1
                    if j:
                        left[i][j] = left[i][j-1] + 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 1:
                    if i != m - 1:
                        bottom[i][j] = bottom[i+1][j] + 1
                    if j != n - 1:
                        right[i][j] = right[i][j+1] + 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    side = min(top[i][j], left[i][j])
                    for k in range(side-1, -1, -1):
                        if k < res:
                            break
                        if min(bottom[i-k][j-k], right[i-k][j-k]) >= k+1:
                            res = max(res, k+1)
                            break

        return res*res

sol = Solution()
grid = [[1,1,1],[1,0,1],[1,1,1]]
assert sol.largest1BorderedSquare(grid) == 9
grid = [[1,1,0,0]]
assert sol.largest1BorderedSquare(grid) == 1
