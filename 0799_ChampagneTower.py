"""
https://leetcode.com/problems/champagne-tower/
The total amount of liquid for i-th row to take is (poured - sum(glass_above_i-th_row)).
We can simulate the process, assume i-th row will hold all the liquid, and pour to the next row when all glasses are full.
Therefore, for the j-th glass in i-th row, the amount of liquid it takes are
dp[i][j] = (dp[i-1][j] - 1) /2 + (dp[i-1][j-1] - 1) / 2
if dp[i][j] - 1 < 0, it has not contribution to the next level.

We can further compress the 2-D dp to 1-D dp to save some space.

Time complexity: O(R^2)
Space complexity: O(R)
"""
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        res = [poured] + [0] * query_row
        for row in range(1, query_row + 1):
            for i in range(row, -1, -1):
                res[i] = max(res[i] - 1, 0) / 2 + max(res[i - 1] - 1, 0) / 2
        return min(res[query_glass], 1)

sol = Solution()
assert sol.champagneTower(1, 1, 1) == 0.0
assert sol.champagneTower(2, 1, 1) == 0.5
