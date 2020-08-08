"""
https://leetcode.com/problems/closest-binary-search-tree-value/

If target < root.val, go to left subtree.
Else go to right subtree.

Time Complexity: O(logN), N = # of nodes in tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        ans = root.val
        while root:
            if abs(root.val - target) < abs(ans - target):
                ans = root.val
            if target > root.val:
                root = root.right
            else:
                root = root.left
        return ans
