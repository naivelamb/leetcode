"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Simple BFS
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode):
        ans = []
        if not root:
            return ans
        curr = [root]
        while curr:
            next = []
            vals = []
            for node in curr:
                vals.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            curr = next
            ans.append(vals)
        return ans[::-1]
