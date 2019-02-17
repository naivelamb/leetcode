# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/cousins-in-binary-tree/solution/

#1 BFS, record the parent and depth
#2 DFS, record the parent and depth
"""
import collections
class Solution:
    def isCousins_bfs(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        parents, depths = {}, {}
        queue = collections.deque((root, 0))
        while queue:
            node, d = queue.popleft()
            if node.left:
                queue.append((node.left, d + 1))
                if node.left.val in (x, y):
                    parents[node.left.val] = node.val
                    depths[node.left.val] = d + 1
            if node.right:
                queue.append((node.right, d + 1))
                if node.right.val in (x, y):
                    parents[node.right.val] = node.val
                    depths[node.right.val] = d + 1
            if len(parents) == 2:
                break
        if len(parents) != 2:
            return False
        if parents[x] != parents[y] and depths[x] == depths[y]:
            return True
        return False
    
    def isCousins_dfs(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        parent, depth = {}, {}
        def dfs(node, par = None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]