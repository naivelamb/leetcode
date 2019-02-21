# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/validate-binary-search-tree/

#1 in-order -> increasing order
#2 Top-down recrusion based on defination
"""
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        vals = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            vals.append(root.val)
            dfs(root.right)
        
        dfs(root)
        for i in range(1, len(vals)):
            if vals[i - 1] >= vals[i]:
                return False
        return True
        
    def isValidBST_recursion(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid(root, -float('inf'), float('inf'))
    
    def is_valid(self, root, min_val, max_val):
        if not root:
            return True
        
        if root.val <= min_val or root.val >= max_val:
            return False
        
        left = self.is_valid(root.left, min_val, root.val)
        right = self.is_valid(root.right, root.val, max_val)
        return left and right