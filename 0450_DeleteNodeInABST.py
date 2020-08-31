"""
https://leetcode.com/problems/delete-node-in-a-bst/

if root.val > key, the node is in left subtree, we do deleteNode(root.left, key)
if root.val < key, the node is in right subtree, we do deleteNode(root.right, key)
if root.val == key, we need to delete root. After delete, we need to find the smallest element in the right subtree, place it at the root position, then we need to delete the smallest element in the right subtree ==> deleteNode(root.right, min_val), where min_val = smallest_element_of (root.right)

Time Complexity: O(H), H = height of the BST
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            # has both left and right
            tmp = root.right
            min_val = tmp.val
            while tmp.left:
                tmp = tmp.left
                min_val = tmp.val
            root.val = min_val
            root.right = self.deleteNode(root.right, root.val)
        return root
