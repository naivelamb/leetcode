# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

Inorder traverse (do right first). 
Time complexity: O(n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.val = 0
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return 
        self.bstToGst(root.right)
        self.val += root.val
        root.val = self.val
        self.bstToGst(root.left)
        return root