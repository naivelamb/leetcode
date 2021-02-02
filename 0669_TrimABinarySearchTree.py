"""
https://leetcode.com/problems/trim-a-binary-search-tree/

Recursion. 

trim(node) ==> return a root/subtree after trim. 

if node.val < low ==> all left subtree are smaller than low, so trim node.right and use the trimed result to replace it. 
if node.val > high ==> all right subtree are larger than high, so trim node.left and use the trimed result to replace it
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trim(node):
            if not node:
                return None
            elif node.val < low:
                return trim(node.right)
            elif node.val > high:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
            return node
        
        return trim(root)