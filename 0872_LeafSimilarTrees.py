# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/leaf-similar-trees/

Sequence can be get by DFS.
Then compare the sequence.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: 'TreeNode', root2: 'TreeNode') -> 'bool':
        def get_seq(root):
            vals = []
            stack = [root]
            while stack:
                node = stack.pop()
                if not node.right and not node.left:
                    vals.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            return vals
        
        vals1, vals2 = get_seq(root1), get_seq(root2)
        if len(vals1) != len(vals2):
            return False
        for i in range(len(vals1)):
            if vals1[i] != vals2[i]:
                return False
        return True

