"""
https://leetcode.com/problems/convert-bst-to-greater-tree/

Iteration with stack
Go to the right most node and store the order to a stack, then go back, add the value together, assign to node. Then go left.
Time complexity: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total, node, stack = 0, root, []
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left
        
        return root