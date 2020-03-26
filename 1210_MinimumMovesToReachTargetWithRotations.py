"""
https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

Use BFS to find the solution.
The state of snake can be marked by head position and tail position

"""
from collections import deque
class Solution:
    def minimumMoves(self, grid) -> int:
        n = len(grid)
        queue = deque()
        queue.append((0, 0, 0, 0, 1))
        visited = set()
        visited.add((0, 0, 0, 1))
        while queue:
            step, tx, ty, hx, hy = queue.popleft()
            if hx == hy == tx == n - 1 and ty == n - 2:
                return step
            # check the cells under the snake
            if hx + 1 < n and grid[hx + 1][hy] == 0 and grid[tx + 1][ty] == 0:
                # move down
                if (tx + 1, ty, hx + 1, hy) not in visited:
                    queue.append((step + 1, tx + 1, ty, hx + 1, hy))
                    visited.add((tx + 1, ty, hx + 1, hy))
                # rotate clockwise
                if tx == hx and (tx, ty, tx +1, ty) not in visited:
                    queue.append((step + 1, tx, ty, tx +1, ty))
                    visited.add((tx, ty, tx +1, ty))
            # check the cells on the right
            if hy + 1 < n and grid[hx][hy + 1] == 0 and grid[tx][ty + 1] == 0:
                # move right
                if (tx, ty + 1, hx, hy + 1) not in visited:
                    queue.append((step + 1, tx, ty + 1, hx, hy + 1))
                    visited.add((tx, ty + 1, hx, hy + 1))
                # move counter clockwise
                if ty == hy and (tx, ty, tx, ty + 1) not in visited:
                    queue.append((step + 1, tx, ty, tx, ty + 1))
                    visited.add((tx, ty, tx, ty + 1))
        return -1


sol = Solution()
grid = [[0,0,0,0,0,1],
       [1,1,0,0,1,0],
       [0,0,0,0,1,1],
       [0,0,1,0,1,0],
       [0,1,1,0,0,0],
       [0,1,1,0,0,0]]
assert sol.minimumMoves(grid) == 11
grid = [[0,0,1,1,1,1],
       [0,0,0,0,1,1],
       [1,1,0,0,0,1],
       [1,1,1,0,0,1],
       [1,1,1,0,0,1],
       [1,1,1,0,0,0]]
assert sol.minimumMoves(grid) == 9
