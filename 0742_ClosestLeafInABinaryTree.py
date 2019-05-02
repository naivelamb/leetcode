# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

Convert tree to graph, then do BFS. 

Time complexity: O(n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def findClosestLeaf(self, root, k):
        graph = collections.defaultdict(list)
        
        def dfs(node, par=None): # build the graph
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        queue = collections.deque(node for node in graph if node and node.val == k)
        seen = set(queue)
        
        while queue:
            node = queue.popleft()
            if node:
                if len(graph[node]) <= 1: #leaf
                    return node.val
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
        
