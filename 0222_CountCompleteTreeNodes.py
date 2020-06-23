"""
https://leetcode.com/problems/count-complete-tree-nodes/
For a node, if we get the same height by going all the way left and all the way right, then the node is a full binary tree, number of nodes = 2**h - 1

Hence, let l & r be the height of tree by going left & right respectively,
if l == r: 2**l - 1
else: 1 + countNodes(root.left) + countNodes(root.right)

l and r can also be achieved recursively.

Time complexity: O(logN), N = # of nodes
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.getDepth(root, True)
        r = self.getDepth(root, False)

        if l == r: # full tree
            return 2**l - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getDepth(self, root, isLeft):
        if not root:
            return 0

        if isLeft:
            return 1 + self.getDepth(root.left, isLeft)
        else:
            return 1 + self.getDepth(root.right, isLeft)
