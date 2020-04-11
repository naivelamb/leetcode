"""
https://leetcode.com/problems/diameter-of-binary-tree/

For a node, if we know the depth of its left subtree and right subtree, then the longest diameter using the node as center is (L + R). So we need to use DFS to get the depth of the tree, and update diameter while we DFS.

Time complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R)
            return max(L, R) + 1
        depth(root)
        return self.ans
