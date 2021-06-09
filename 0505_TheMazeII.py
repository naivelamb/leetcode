"""
https://leetcode.com/problems/the-maze-ii/

Dijkstra + PQ

time complexity: O(mnlog(mn))
"""
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = [(0, start[0], start[1])]
        heapq.heapify(queue)
        m, n = len(maze), len(maze[0])
        dists = [[float('inf')] * n for _ in range(m)]
        dists[start[0]][start[1]] = 0
        while queue:
            step, i, j = heapq.heappop(queue)
            if i == destination[0] and j == destination[1]:
                return step
            
            for di, dj in dirs:
                new_i, new_j = i + di, j + dj
                tmp = step + 1
                while 0 <= new_i < m and 0 <= new_j < n and maze[new_i][new_j] != 1:
                    new_i += di
                    new_j += dj
                    tmp += 1
                new_i -= di
                new_j -= dj
                tmp -= 1
                if tmp < dists[new_i][new_j]:
                    dists[new_i][new_j] = tmp
                    heapq.heappush(queue, (tmp, new_i, new_j))
        return -1        