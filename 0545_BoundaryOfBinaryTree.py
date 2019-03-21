# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/boundary-of-binary-tree/

Modified preorder 

Time complexity: O(n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode):
        if not root: return []
        res = [root.val]
        
        def dfs(root, isLeft, isRight):
            if root:
                # leaf node or left node
                if (not root.left and not root.right) or isLeft:
                    res.append(root.val)
                
                if root.left and root.right:
                    dfs(root.left, isLeft, False)
                    dfs(root.right, False, isRight)
                else:
                    dfs(root.left, isLeft, isRight)
                    dfs(root.right, isLeft, isRight)
                
                if (root.left or root.right) and isRight:
                    res.append(root.val)
        
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return res
        
        
        
