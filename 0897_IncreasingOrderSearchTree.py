# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/increasing-order-search-tree/

#1 Iterative method
In-order traversal the tree. Then build the new tree. 

#2 Recrusive
While in-order traversal, live link the tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: 'TreeNode') -> 'TreeNode':
        vals = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        inorder(root)
        
        dummy = pre = TreeNode(None)
        for val in vals:
            pre.right = TreeNode(val)
            pre = pre.right
        return dummy.right
    
    def increasingBST_recursive(self, root):
        ans = self.cur = TreeNode(None)
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            root.left = None
            self.cur.right = root
            self.cur = root
            inorder(root.right)
        
        inorder(root)     
        return ans.right      