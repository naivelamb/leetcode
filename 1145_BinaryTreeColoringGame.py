"""
https://leetcode.com/problems/binary-tree-coloring-game/

Compare count of nodes of the neighboring node of x.
Need to take care of parent situation.
If l is the # of nodes in the left subtree, r is the # of nodes in the right subtree,
then the # of nodes in parent subtree is n - l - r
If someone can get (n // 2 + 1) nodes, he wins automatically.

To make sure win, 2nd player should choose a node that is connected to 1st player's node.

Use DFS to count all the nodes of all subtrees.
Time complexity: O(n)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        cnt = [0, 0] # count left & right leaf of node x
        def count(node):
            if not node:
                return 0
            l, r = count(node.left), count(node.right)
            if node.val == x:
                cnt[0], cnt[1] = l, r
            return l + r + 1

        return count(root)/2 < max(max(cnt), n - sum(cnt) - 1)
