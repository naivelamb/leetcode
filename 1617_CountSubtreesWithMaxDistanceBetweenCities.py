"""
https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

Try all potential subgraphs, check if they can form a tree. If so find the diameter.

To check if they form a tree, we can use bfs go from one node, we can visited all nodes, then it can form a tree. To find the diameter, we can first randomly pick a node, go to the end, then do bfs from the end node to find the maximum distance, which would be the diameter.

Time complexity: O(n*2^n)
"""
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        def bfs(src, graph):
            visited = {src}
            q = collections.deque([(src, 0)])
            farthestNode, farthestDist = -1, 0
            while q:
                farthestNode, farthestDist = u, d = q.popleft()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, d+1))
            return farthestNode, farthestNode, visited

        def diameterOfTree(cities, graph):
            anyNode = cities.pop()
            cities.add(anyNode)
            farthestNode, _, visited = bfs(anyNode, graph)
            if len(visited) < len(cities): return 0
            _, dist, _ = bfs(farthestNode, graph)
            return dist

        def maxDistance(state):
            cities = set()
            for i in range(n):
                if (state >> i) & 1 == 1:
                    cities.add(i)
            graph = collections.defaultdict(list)
            for u, v in edges:
                u, v = u - 1, v - 1
                if u in cities and v in cities:
                    graph[u].append(v)
                    graph[v].append(u)
            return diameterOfTree(cities, graph)

        ans = [0] * (n - 1)
        for state in range(1, 2**n):
            d = maxDistance(state)
            if d > 0: ans[d-1] += 1
        return ans
