# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Recursive. 
helper(root) return head, tail after flatten tree based on root.
Base case:
    if not root:
        return None, None
    if not root.left and not root.right:
        return root, root
l_head, l_tail = helper(root.left)
r_head, r_tail = helper(root.right)
root.left = None
root.right = l_head if l_head else r_head
if l_tail: l_tail.right = r_head
tail = r_tail if r_head else l_tail
return root, tail

"""

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if not root:
                return None, None
            if not root.left and not root.right:
                return root, root
            l_head, l_tail = helper(root.left)
            r_head, r_tail = helper(root.right)
            root.left = None
            root.right = l_head if l_head else r_head
            if l_tail:
                l_tail.right = r_head
            tail = r_tail if r_head else l_tail
            return root, tail
        helper(root)