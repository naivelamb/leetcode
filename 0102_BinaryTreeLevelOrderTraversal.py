# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Typical BFS
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        res = []
        if not root:
            return res
        curr_level = [root]
        while curr_level:
            next_level = []
            curr_vals = []
            for node in curr_level:
                curr_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(curr_vals)
            curr_level = next_level
        return res        