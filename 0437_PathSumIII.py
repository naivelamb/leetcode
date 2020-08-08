"""
https://leetcode.com/problems/path-sum-iii/

When traverse down to a node N, we store the sum until this node (sum_so_far(prefix) + N.val) in a hashtable. This is the sum from root to the node N.

Then for the grand-child of N, called it G, we can get the prefix sum from root to G.

Let's say if some node A is the predecessor of G, and sum(root -> G) - sum(root -> A) = target, so at Node G we need to look for
sum_so_far + G.val - target in the hashtable.

Time complexity: O(N), since every node is visited once. 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result

    def helper(self, root, target, so_far, cache):
        if root:
            complement = so_far + root.val - target
            if complement in cache:
                self.result += cache[complement]
            cache.setdefault(so_far + root.val, 0)
            cache[so_far + root.val] += 1
            self.helper(root.left, target, so_far + root.val, cache)
            self.helper(root.right, target, so_far + root.val, cache)
            cache[so_far + root.val] -= 1
        return
