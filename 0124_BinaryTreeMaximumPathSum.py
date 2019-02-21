# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

dfs, return s1, s2
s1: max sum ending at node
s2: max sum not ending at node

s1 = max(node.val, node.val + ls1, node.val + rs1)
s2 = max(ls1, ls2, rs1, rs2, node.val + ls1 + rs2)
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: 'TreeNode') -> 'int':
        def dfs(node):
            if not node:
                return -float('inf'), -float('inf')
            ls1, ls2 = dfs(node.left)
            rs1, rs2 = dfs(node.right)
            
            s1 = max(node.val, node.val + ls1, node.val + rs1)
            s2 = max(ls1, ls2, rs1, rs2, node.val + ls1 + rs1)
            return s1, s2
        
        return max(dfs(root))