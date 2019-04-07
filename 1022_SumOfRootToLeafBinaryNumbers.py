# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

BFS, add when moving to leaf

Time complexity: O(n), n -> number of nodes
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
import collections
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = 0
        queue = collections.deque([])
        queue.append((root, str(root.val)))
        while queue:
            curr, val = queue.popleft()
            if not curr.left and not curr.right: #leaf
                res += int(val, 2)
            if curr.left:
                queue.append((curr.left, val + str(curr.left.val)))
            if curr.right:
                queue.append((curr.right, val + str(curr.right.val)))
        return res % (10**9 + 7)