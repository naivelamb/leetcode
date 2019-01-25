# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/sum-of-distances-in-tree/

Brute Force:
Given root, we can get sum of all its distances in O(N). We do this for all 
nodes, we can get the result in O(N^2). => TLE

Take the following tree as example 
       0
      / \
     1   2
        /|\
       3 4 5
When calculate the sum distance to root 0, we use dfs to compute all its subtree
sum distance. We will have, dist(3) = dist(4) = dist(5) = 0, dist(2) = 3, 
dist(1) = 0, dist(0) = 0 + 1 + 3 + 4 = 8
How we compute it? For each node, we need to know its sum distance of its children,
and the count of nodes in it. Then,
dist(root) = sum(dist(root.child)) + sum(count(root.child))

What would happen if we now use 2 as the root? Comparing to using root 0, all 
nodes belong to root 2 is 1 step closer, the rest nodes is 1 step away. 
dist(2) = dist(0) - count(2) + N - count(2) = 8 - 4 + 6 - 4 = 6
In other words,
dist(node) = dist(parent) - count(node) + N - count(node)

We do this from root layer by layer (BFS), we can solve this in O(N)
"""
import collections
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # build the tree
        graph = collections.defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        dist = [0] * N
        count = [0] * N
        
        def dfs(root, seen):
            # Given a root, compute its sum distance and nodes belong to it 
            seen.add(root)
            for i in graph[root]:
                if i not in seen:
                    dfs(i, seen)
                    count[root] += count[i]
                    dist[root] += dist[i] + count[i]
            count[root] += 1
        
        dfs(0, set())
        
        q = collections.deque([(x, 0) for x in graph[0]])
        seen = set([0])
        while q:
            node, parent = q.popleft()
            if node in seen:
                continue
            seen.add(node)
            dist[node] = dist[parent] - count[node] + N - count[node]
            for child in graph[node]:
                q.append((child, node))
        return dist
        