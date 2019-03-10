# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

Do it recursive. Given a node and the range, we know the range of its left 
subtree as well as its right subtree.

Time complexity: O(n) => since all element in the preorder is visited only once.  
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        self.idx = 0
        size = len(preorder)
        def helper(preorder, mini, maxi, size):
            if self.idx >= size:
                return None
            val = preorder[self.idx]
            root = None
            if mini < val < maxi:
                root = TreeNode(val)
                self.idx += 1
                if self.idx < size:
                    root.left = helper(preorder, mini, val, size)
                    root.right = helper(preorder, val, maxi, size)
            return root
        
        return helper(preorder, float('-inf'), float('inf'), size)
