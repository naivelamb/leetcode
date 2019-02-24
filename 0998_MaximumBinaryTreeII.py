# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/maximum-binary-tree-ii/

val is append the end of the array, therefore it can only be add to the right 
child

Time Complexity: O(logN)
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        if root.val < val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        if not root.right:
            root.right = TreeNode(val)
            return root
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
