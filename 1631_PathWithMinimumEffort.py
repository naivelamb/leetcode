"""
https://leetcode.com/problems/path-with-minimum-effort/

Dijkstra
Time complexity: O(MNlogMN)
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        q = [(0, 0, 0)]
        seen = set()
        while q:
            cost, i, j = heapq.heappop(q)
            if (i, j) == (m-1, n-1):
                return cost
            if (i, j) in seen:
                continue
            seen.add((i, j))
            for ni, nj in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= ni < m and 0 <= nj < n:
                    if (ni, nj) not in seen:
                        price = abs(heights[i][j] - heights[ni][nj])
                        heapq.heappush(q, (max(price, cost), ni, nj))
        return -1