"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        current_level = 0
        nodes = [root]
        while nodes:
            tmp = []
            vals = []
            for node in nodes:
                vals.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if current_level % 2 == 0:
                ans.append(vals)
            else:
                ans.append(vals[::-1])
            current_level += 1
            nodes = tmp
        return ans        
