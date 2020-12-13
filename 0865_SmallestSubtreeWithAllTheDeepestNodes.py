"""
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

1) Find all the deepest nodes.
2) Find LCA for the left-most and right-most nodes. 

Time complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        stack = [root]
        while stack:
            tmp = []
            for node in stack:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            if not tmp:
                break
            else:
                stack = tmp
        
        return self.lca(root, stack[0], stack[-1])

    def lca(self, root, p, q):
        if not root:
            return
        
        if p == root or q == root:
            return root
        
        left = right = None
        if root.left:
            left = self.lca(root.left, p, q)
        if root.right:
            right = self.lca(root.right, p, q)
        
        return root if left and right else left or right