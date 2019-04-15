# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

For a given node, we need to know the maximum and minimum in its subtree. Then 
res = max(res, abs(node.val - min), abs(node.val - max))

Time complexity: O(n)
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root):
        def helper(node, mn, mx):
            if not node:
                return mx - mn
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            return max(helper(node.left, mn, mx), helper(node.right, mn, mx))
        
        return helper(root, root.val, root.val)

