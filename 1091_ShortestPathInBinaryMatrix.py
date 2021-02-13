"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/

BFS + Heap 
Time complexity: O(MNlogMN)
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set()
        heap = [(1, 0, 0)]
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        while heap:
            step, i, j = heapq.heappop(heap)
            if (i, j) == (n-1, n-1):
                return step
            if (i, j) in visited:
                continue
            # valid move, store next potential step
            visited.add((i, j))
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < n and 0 <= new_j < n and grid[new_i][new_j] == 0 and (new_i, new_j) not in visited:
                    heapq.heappush(heap, (step + 1, new_i, new_j))
        return -1