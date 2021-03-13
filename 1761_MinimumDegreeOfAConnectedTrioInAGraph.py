"""
https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

Build graph. Then brute force. 

For two nodes, we find the nodes in their intersected connected nodes => trio. 
Degree = sum(nodes connected to these 3 nodes) - 6

Pruning the nodes.

Time complexity: O(N^3)
"""
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        d = collections.defaultdict(int)
        for n in graph:
            d[n] = len(graph[n])
        
        res = float('inf')
        for a in graph:
            for b in graph[a]:
                for c in graph[a] & graph[b]:
                    res = min(res, d[a] + d[b] + d[c] - 6)
                    if a in graph[c]:
                        graph[c].remove(a)
                if a in graph[b]:
                    graph[b].remove(a)

        if res == float('inf'):
            return -1
        else:
            return res