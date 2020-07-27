"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Inorder: left, root, right
# Postorder: left, right, root
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return

        root = TreeNode(val=postorder[-1])
        idx = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
        return root

    def buildTree_recur(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i

        def helper(low, high):
            if low > high:
                return None
            root = TreeNode(postorder.pop())
            mid = map_inorder[root.val]
            root.right = helper(mid+1, high)
            root.left = helper(low, mid-1)
            return root

        return helper(0, len(inorder) - 1)
