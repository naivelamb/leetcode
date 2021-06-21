"""
https://leetcode.com/problems/swim-in-rising-water/

Dijkstra, always go the the smallest point next. 

Time complexity: O(N^2logN)
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        seen = {(0, 0)}
        pq = [(grid[0][0], 0, 0)]
        ans = 0
        while pq:
            d, i, j = heapq.heappop(pq)
            ans = max(ans, d)
            if i == j == N - 1: return ans
            for ni, nj in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in seen:
                    heapq.heappush(pq, (grid[ni][nj], ni, nj))
                    seen.add((ni, nj))