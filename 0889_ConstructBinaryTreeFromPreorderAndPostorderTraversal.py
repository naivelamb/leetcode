# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

Preorder: root, left, right
Postorder: left, right, root

number of nodes in left subtree: L = Postorder.index(preorder[1]) + 1
left = construct(preorder[1: L + 1], postorder[:L])
right = construct(preorder[L+1:], postorder[L:-1])

Time complexity: O(n^2)
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root
        
        L = post.index(pre[0]) + 1
        root.left = self.constructFromPrePost(pre[1: L + 1], post[: L])
        root.right = self.constructFromPrePost(pre[L + 1:], post[L: -1])
        return root
        
        
