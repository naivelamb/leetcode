"""
https://leetcode.com/problems/house-robber-iii/

Each node has two state: rob or not rob, it will influence the results of its subtree. 

We need to know:
1) your max gain if you rob current node --> v1
2) your max gain if you skip current node --> v2

v1[parent] = node.val + v2[node.left] + v2[node.right]
v2[parent] = max(v1[node.left], v2[node.left]) + max(v1[node.right], v2[node.right])

Time complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left = dfs(node.left)
            right = dfs(node.right)
            return (node.val + left[1] + right[1]), max(left) + max(right)
        
        return max(dfs(root))
