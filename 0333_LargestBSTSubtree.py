# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/largest-bst-subtree/

For a node, we need to know the following information:
    1. How many nodes in the subtree using it as root
    2. Min value in the subtree
    3. Max value in the subtree
    4. Is the subtree BST

For a node, if we know the above information about its two children, we know
the information about the subtree using it as root.

We use recursion to solve the problem. 

Time complexity: O(n), since all the nodes are visited only once.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        def helper(node):
            if not node:
                return 0, float('inf'), -float('inf'), True
            
            n_left, min_left, max_left, state_left = helper(node.left)
            n_right, min_right, max_right, state_right = helper(node.right)
            
            n_root = n_left + n_right + 1
            min_root = min(min_left, min_right, node.val)
            max_root = max(max_left, max_right, node.val)
            state_root = (state_left and state_right and (max_left < node.val < min_right))
            
            if state_root:
                self.ans = max(self.ans, n_root)
            
            return n_root, min_root, max_root, state_root
        
        helper(root)
        return self.ans