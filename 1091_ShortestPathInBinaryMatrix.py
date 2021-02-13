"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/

BFS
Time complexity: O(MN)
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = collections.deque([(1, 0, 0)])
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        while queue:
            step, i, j = queue.popleft()
            if (i, j) == (n-1, n-1):
                return step
            if (i, j) in visited:
                continue
            # valid move, store next potential step
            visited.add((i, j))
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == 0 and (new_i, new_j) not in visited:
                    queue.append((step + 1, new_i, new_j))
        return -1