"""
https://leetcode.com/problems/balanced-binary-tree/

DFS. 
helper(node): return is_balanced, node_height
If either left or left is not balanced, return False. 
Else: check if height difference is no more than 1. Then compute height: max(l_h, r_h) + 1

Time complexity: O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if not node:
                return True, 0
            l, lh = helper(node.left)
            r, rh = helper(node.right)
            if not l or not r:
                return False, 0
            if abs(lh - rh) <= 1:
                return True, max(lh, rh) + 1
            else:
                return False, 0
        ans, _ = helper(root)
        return ans