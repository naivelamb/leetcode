"""
https://leetcode.com/problems/pacific-atlantic-water-flow/

BFS
Time complexity: O(mn)
"""
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []

        m, n = len(matrix), len(matrix[0])

        def bfs(starts):
            queue = collections.deque(starts)
            visited = set(starts)
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]:
                    if 0 <= dx < m and 0 <= dy < n and (dx, dy) not in visited and matrix[dx][dy] >= matrix[x][y]:
                        queue.append((dx, dy))
                        visited.add((dx, dy))

            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m-1, i) for i in range(n)] + [(i, n-1) for i in range(m-1)]
        
        return list(bfs(pacific) & bfs(atlantic))   