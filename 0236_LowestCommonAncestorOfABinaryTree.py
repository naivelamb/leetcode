# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

If p or q is the root, then root is LCA
Else, need to look into root.left or root.right

"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        if p == root or q == root:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left        