# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/maximum-width-of-binary-tree/

BFS. Each node is marked by (height, idx, node)
If node.left != None, add (height + 1, 2 * idx - 1, node.left) to queue.
If node.right != None, add (height + 1, 2 * idx, node.right) to queue.

Time complexity: O(n), n => total nodes in the tree.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        ref = collections.defaultdict(list)
        ref[0] = [1]
        ans = 1
        queue = collections.deque([(0, 1, root)])
        while queue:
            h, idx, node = queue.popleft()
            ref[h].append(idx)
            ans = max(ans, ref[h][-1] - ref[h][0] + 1)
            if node.left:
                queue.append((h + 1, 2*idx - 1, node.left))
            if node.right:
                queue.append((h + 1, 2*idx, node.right))
        return ans
