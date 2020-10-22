"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

BFS/DFS to traverse all nodes, find the minimum depth. 

Time complexity: O(N), N = # of nodes
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [[root, 1]]
        ans = float('inf')
        while stack:
            node, depth = stack.pop()
            if node.left or node.right:
                if node.left:
                    stack.append([node.left, depth + 1])
                if node.right:
                    stack.append([node.right, depth + 1])
            else:# leaf node
                ans = min(ans, depth)
        return ans