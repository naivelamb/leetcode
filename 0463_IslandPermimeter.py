"""
https://leetcode.com/problems/island-perimeter/

# of neighbor, contribution to perimeter:
0, 4
1, 3
2, 2
3, 1
4, 0
Count neighbor of all island block, can get perimeter.

Time complexity: O(MN), M = len(grid), N = len(grid[0])
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt = 0
                    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        x, y = i + di, j + dj
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            cnt += 1
                    ans += 4 - cnt
        return ans
