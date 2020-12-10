"""
https://leetcode.com/problems/spiral-matrix-ii/

Simulation
Time complexity: O(N^2)
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, j = 0, 0
        d = 0
        for x in range(1, n**2 + 1):
            res[i][j] = x
            dx, dy = dirs[d]
            cnt = 0
            while i + dx >= n or i + dx < 0 or j + dy >= n or j + dy < 0 or res[i+dx][j+dy] != 0:
                d += 1
                if d >= 4:
                    d %= 4
                dx, dy = dirs[d]
                cnt += 1
                if cnt == 4:
                    break
            i += dx
            j += dy
        return res  