# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/closest-binary-search-tree-value-ii/

BST inorder gives the non-decreasing array. We do inorder and keep track of the 
res. When length is larger than k, we decide whether pop left and append right. 

Time complexity: O(n)
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if len(res) < k:
                res.append(root.val)
            elif abs(res[0] - target) > abs(root.val - target):
                res.popleft()
                res.append(root.val)
            else:
                return
            inorder(root.right)
        
        res = collections.deque([])
        inorder(root)
        return list(res)