"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        vals = []

        def dfs(root, curr):
            if not root.left and not root.right:
                vals.append(curr*10 + root.val)
                return
            if root.left:
                dfs(root.left, curr*10 + root.val)
            if root.right:
                dfs(root.right, curr*10 + root.val)
                
        dfs(root, 0)
        return sum(vals)
