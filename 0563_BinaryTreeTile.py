"""
https://leetcode.com/problems/binary-tree-tilt/
DFS, each node return subtree sum. 

Time complexity: O(N)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            
            v_left, v_right = dfs(node.left), dfs(node.right)
            self.ans += abs(v_left - v_right)
            return (v_left + v_right + node.val)
        
        dfs(root)
        return self.ans