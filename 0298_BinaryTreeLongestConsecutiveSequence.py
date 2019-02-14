# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

1. BFS. 
Put (node, l) into queue. l -> length of consecutive sequence ending at 
the node. If node.left.val == node.val + 1, then put (l + 1) into queue. 

2. Bottom-up DFS
Use a helper dfs(node) function, which return the maximum consecutive length 
starting at node. 
Then for a node, 
L = dfs(node.left) + 1 if node.left.val == node.val + 1, else L = 1
R = dfs(node.right) + 1 if node.right.val == node.val + 1, else R = 1
Length = max(L, R)

"""
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: 'TreeNode') -> 'int':
        res = 0
        if not root:
            return res
        queue = collections.deque([(root, 1)])
        while queue:
            node, l = queue.popleft()
            res = max(res, l)
            if node.left:
                if node.left.val == node.val + 1:
                    queue.append((node.left, l + 1))
                else:
                    queue.append((node.left, 1))
            if node.right:
                if node.right.val == node.val + 1:
                    queue.append((node.right, l + 1))
                else:
                    queue.append((node.right, 1))
        return res

    def longestConsecutive_dfs(self, root: 'TreeNode') -> 'int':
        self.maximum = 0
        def dfs(node):
            if not node:
                return 0
            L = dfs(node.left) + 1
            R = dfs(node.right) + 1
            if node.left and node.left.val != node.val + 1:
                L = 1
            if node.right and node.right.val != node.val + 1:
                R = 1
            length = max(L, R)
            self.maximum = max(self.maximum, length)
            return length
        dfs(root)
        return self.maximum