"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Simple DFS/BFS
Time complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            
            return max(dfs(node.left), dfs(node.right)) + 1
        
        return dfs(root)