"""
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

All values are unique, just traverse the cloned tree and find the node with the target value.
Time complexity: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [cloned]
        while stack:
            node = stack.pop()
            return node if node.val == target.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)