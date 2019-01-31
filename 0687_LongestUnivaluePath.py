# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-univalue-path/

We will solve the problem recursively.
Let helper(node) return the longest path that starts at node. 
left_len, right_len -> helper(node.left), helper(node.right)
Then the longest path starts from node is:
    left = left_len + 1 if node.val == node.left.val else 0
    right = right_len + 1 if node.val == node.right.val else 0
The longest path including the node is left + right.
Recursion done from the bottom, need to compare (left + right) with current max
path.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def helper(node):
            if not node:
                return 0
            left_len, right_len = helper(node.left), helper(node.right)
            if node.left and node.left.val == node.val:
                left = left_len + 1 
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right = right_len + 1
            else:
                right = 0
            self.ans = max(self.ans, left + right)
            return max(left, right)
        helper(root)
        return self.ans
