"""
https://leetcode.com/problems/map-of-highest-peak/

Find all water node, then use them as source, BFS.

Time comlexity: O(MN)
"""
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        water = set()
        m, n = len(isWater), len(isWater[0])
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    water.add((i, j))
        
        heights = [[0] * n for _ in range(m)]
        seen = water
        queue = collections.deque([[0, i, j] for i, j in water])
        while queue:
            h, i, j = queue.popleft()
            for (di, dj) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_i, new_j = i + di, j + dj
                if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in seen:
                    seen.add((new_i, new_j))
                    queue.append((h + 1, new_i, new_j))
                    heights[new_i][new_j] = h + 1
                else:
                    pass
        return heights
            