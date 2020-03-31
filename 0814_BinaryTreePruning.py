"""
https://leetcode.com/problems/binary-tree-pruning/

Recursion.
hasOne(node) -> return True if the subtree using node as root contains one. And do the pruning.


"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def hasOne(node):
            if not node:
                return False
            a1 = hasOne(node.left)
            a2 = hasOne(node.right)
            if not a1:
                node.left = None
            if not a2:
                node.right = None
            return node.val == 1 or a1 or a2
        return root if hasOne(root) else None
