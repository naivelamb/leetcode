"""
https://leetcode.com/problems/binary-tree-cameras/

Node has 3 possible state:
1. all nodes below this node are covered, but not this node
2. all nodes including this node are covered, but no camera
3. camera on this node. 

let dp0, dp1,dp3 be the minimum cameras for the above states respectively, and dfs(node) return (dp0, dp1, dp2) for the node. Let
Then for the node, we know,

dp0 = dp1_L + dp1_R
dp1 = min(dp2_L + min(dp1_R, dp2_R), dp2_R + min(dp1_L, dp2_L))
dp2 = 1 + min(dp0_L, dp1_L, dp2_L) + min(dp0_R, dp1_R, dp2_R)

Time complexity: O(N), N = # of nodes
"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, 0, float('inf')
            L = dfs(node.left)
            R = dfs(node.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)
            return dp0, dp1, dp2
        
        return min(dfs(root)[1:])