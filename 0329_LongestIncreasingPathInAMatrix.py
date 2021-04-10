"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

dp[i][j]: longest path using [i][j] as start. 
dfs(i, j): return longest path using (i, j) as start. 

For an abitrary (i, j), check its 4 neighbors such that martrix[x][y] > matrix[i][j], 
dp[i][j] = max(dp[x][y]) + 1

Time complexity: O(mn)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        dp = [[0] * len(matrix[0]) for _ in matrix]
        all_len = []

        def dfs(i, j):
            if dp[i][j] == 0: #unvisited
                tmp = []
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    x, y = i + di, j + dj
                    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                        tmp.append(dfs(x, y))
                    if tmp:
                        dp[i][j] = 1 + max(tmp)
                    else:
                        dp[i][j] = 1
            return dp[i][j]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                all_len.append(dfs(i, j))
        return max(all_len)