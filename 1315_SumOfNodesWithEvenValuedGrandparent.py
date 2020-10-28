"""
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

Traverse the tree, for each node, we record (node, parent_val, grandparent_val)
If grandparent_val % 2 == 0, we add the node.val to ans.

Time compelxity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        stack = [(root, None, None)]
        while stack:
            node, parent, grandparent = stack.pop()
            if grandparent and grandparent % 2 == 0:
                ans += node.val
            if node.left:
                stack.append((node.left, node.val, parent))
            if node.right:
                stack.append((node.right, node.val, parent))
        return ans