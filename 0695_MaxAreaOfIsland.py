"""
https://leetcode.com/problems/max-area-of-island/

DFS, mark all visited positions as 0. 

Time complexity: O(mn)
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] == 0:
                return 0
            
            ans = 1
            grid[r][c] = 0
            for dr, dc in DIR:
                ans += dfs(r + dr, c + dc)
            return ans
        
        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))
        return ans