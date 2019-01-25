# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/recover-binary-search-tree/

In-order traversal of BST gives sorted array. 

If two neighbor nodes are swapped, we will find one pair such that prev.val > curr.val
If two non-neighbor nodes are swapped, we will find two pairs. 

We will swap the first node in the first pair and the second node in the second pair.
"""
class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        curr, prev, drop, stack = root, TreeNode(float('-inf')), [], []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                if node.val < prev.val: # wrong pair
                    drop.append((prev, node))
                prev, curr = node, node.right
        drop[0][0].val, drop[-1][1].val = drop[-1][1].val, drop[0][0].val
