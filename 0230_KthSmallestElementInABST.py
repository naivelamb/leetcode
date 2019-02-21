# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

#1 Naive Way:
In order traversal the tree, then get the K-th element. 

#2 In order together with the count
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: 'TreeNode', k: 'int') -> 'int':
        curr, stack = root, []
        cnt = 0
        while stack or root:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                cnt += 1
                if cnt == k:
                    return curr.val
                curr = curr.right