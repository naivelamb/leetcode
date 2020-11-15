"""
https://leetcode.com/problems/range-sum-of-bst/

DFS
Time complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def helper(node, l, h):
            if not node:
                return 0
            
            tmp = 0
            if l <= node.val <= h:
                tmp += node.val
            return tmp + helper(node.left, l, h) + helper(node.right, l, h)