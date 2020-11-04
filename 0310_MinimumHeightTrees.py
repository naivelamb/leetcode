"""
https://leetcode.com/problems/minimum-height-trees/

Build the graph -> O(E)
Find the end node -> O(E)
Go from the end node toward center (BFS), when we ends up with one node and no next level, or two nodes that are coming together in next level, we find the roots. -> O(E)

Time complexity: O(V + E)
"""
import collections
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        # build graph
        neighbors = collections.defaultdict(list)
        degrees = collections.defaultdict(int)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        
        preLevel, unvisited = [], set(range(n))
        for i in range(n):
            if degrees[i] == 1:
                preLevel.append(i)
        
        while len(unvisited) > 2:
            currLevel = []
            for u in preLevel:
                unvisited.remove(u)
                for v in neighbors[u]:
                    if v in unvisited:
                        degrees[v] -= 1
                        if degrees[v] == 1:
                            currLevel.append(v)
            preLevel = currLevel
        return preLevel