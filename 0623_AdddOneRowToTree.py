"""
https://leetcode.com/problems/add-one-row-to-tree/

First check whether we need to add the new node as root. 

Else use either BFS/DFS to trasverse the tree. When we meet (d - 1) depth, we need to add layer.

Time complexity: O(N)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        
        stack = [(1, root)]
        while stack:
            depth, curr = stack.pop()
            if depth == d - 1: #add new node
                left, right = curr.left, curr.right
                curr.left, curr.right = TreeNode(v), TreeNode(v)
                if left:
                    curr.left.left = left
                if right:
                    curr.right.right = right
            else:
                if curr.left:
                    stack.append((depth + 1, curr.left))
                if curr.right:
                    stack.append((depth + 1, curr.right))
        return root