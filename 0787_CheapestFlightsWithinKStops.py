"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/

First build graph, graph[i][j] = k, means from i to j, the price is k (path weight).
Next, use BFS to go maximum k steps, find the cheapest path sum to dst.
"""
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        costs = [float('inf')] * n
        costs[src] = 0
        q = collections.deque()
        q.append((src, 0, K+1))
        while q:
            curr, cost, stops = q.popleft()
            if stops == 0: # used all stops
                break
            for nei in graph[curr]:
                new_cost = graph[curr][nei] + cost
                if new_cost < costs[nei]:
                    costs[nei] = new_cost
                    q.append((nei, new_cost, stops - 1))
        return costs[dst] if costs[dst] < float('inf') else -1
