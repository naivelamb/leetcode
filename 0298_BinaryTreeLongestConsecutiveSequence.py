# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

BFS. Put (node, l) into queue. l -> length of consecutive sequence ending at 
the node. If node.left.val == node.val + 1, then put (l + 1) into queue. 
"""
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: 'TreeNode') -> 'int':
        res = 0
        if not root:
            return res
        queue = collections.deque([(root, 1)])
        while queue:
            node, l = queue.popleft()
            res = max(res, l)
            if node.left:
                if node.left.val == node.val + 1:
                    queue.append((node.left, l + 1))
                else:
                    queue.append((node.left, 1))
            if node.right:
                if node.right.val == node.val + 1:
                    queue.append((node.right, l + 1))
                else:
                    queue.append((node.right, 1))
        return res