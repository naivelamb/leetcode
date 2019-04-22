# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/sum-of-left-leaves/

BFS
Time complexity: O(n)
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return res
        deque = collections.deque([root])
        while deque:
            node = deque.popleft()
            if node.left:
                deque.append(node.left)
                if not node.left.left and not node.left.right:
                    res += node.left.val
            if node.right:
                deque.append(node.right)
        return res
