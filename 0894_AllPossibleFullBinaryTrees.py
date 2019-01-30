# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/all-possible-full-binary-trees/

If N % 2 == 0, no full binary tree
If N = 2k + 1, then we need to find all possible ways to distribute L nodes to 
the left, R nodes to the right, where both L and R are odd numbers and L + R == 2k.
The possible subtrees for L nodes are basically all possible full binary trees
for L. 

Therefore, the problem can be solved recursively 
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        # use cache to store the result for N, save space
        cache = {}
        def helper(N):
            # Given N, return all possible binary trees
            if N in cache:
                return cache[N]
            # Return None if N is an even number
            if N % 2 == 0:
                return []
            # Base case
            if N == 1:
                cache[1] = [TreeNode(0)]
                return cache[1]
            # Get the nodes in left and right
            l, r = 1, N - 2
            res = []
            while l <= N - 2:
                l_subtrees, r_subtrees = helper(l), helper(r)
                for l_root in l_subtrees:
                    for r_root in r_subtrees:
                        root = TreeNode(0)
                        root.left, root.right = l_root, r_root
                        res.append(root)
                l += 2
                r -= 2
            cache[N] = res
            return cache[N]
        return helper(N)