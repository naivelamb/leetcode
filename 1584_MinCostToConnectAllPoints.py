"""
https://leetcode.com/problems/min-cost-to-connect-all-points/
Minimum spanning tree, Prim's algorithm.
Time Complexity: O(V^2 + (E+V)logV)

"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build graph
        n = len(points)
        graph = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    p1, p2 = points[i], points[j]
                    d = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                    graph[i][j] = d
                    graph[j][i] = d

        start = res = 0
        visited = {start}
        min_heap = []
        for cost, adj in graph[start]:
            heapq.heappush(min_heap, (cost, adj))

        while len(visited) < len(points) + 1 and min_heap:
            cost, next_node = heapq.heappop(min_heap)
            if next_node not in visited:
                visited.add(next_node)
                res += cost
                for next_cost, adj in graph[next_node]:
                    if adj not in visited:
                        heapq.heappush(min_heap, (next_cost, adj))
        return res
