"""
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/532/week-5/3315/
BFS, prune nodes if it does not match the sequence

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr) -> bool:
        if not root:
            return False
        curr_level = [root]
        for i, val in enumerate(arr):
            next_level = []
            for node in curr_level:
                if node.val == val:
                    if i == len(arr) - 1:
                        if not (node.left or node.right):
                            return True
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
            curr_level = next_level
        return False
