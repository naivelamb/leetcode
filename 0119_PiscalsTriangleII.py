"""
https://leetcode.com/problems/pascals-triangle-ii/

DP[i] -> row value for row-index i
DP[i+1][j] = DP[i][j] + DP[i][j-1] for j >= 1

In order to only use O(k) extra space, we do the DP from right to left.

Time Complexity: O(k^2)
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1] + [0] * rowIndex
        for i in range(rowIndex + 1):
            for j in range(0, i):
                ans[i-j] += ans[i-j-1]
        return ans
