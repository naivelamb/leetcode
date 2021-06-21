"""
https://leetcode.com/problems/pascals-triangle/
dp. 
dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * (i+1) for i in range(numRows)]

        for i in range(0, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res