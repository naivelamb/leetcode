"""
https://leetcode.com/problems/even-odd-tree/

BFS, check the tree level by level.

Time complexity: O(N)
"""
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = [root]
        is_even = True
        while queue:
            newq = []
            prev = float(-inf) if is_even else float(inf)
            for node in queue:
                if is_even:
                    if (node.val % 2 == 0) or (node.val <= prev):
                        return False
                else:
                    if (node.val % 2 == 1) or (node.val >= prev):
                        return False
                if node.left:
                    newq.append(node.left)
                if node.right:
                    newq.append(node.right)
                prev = node.val
            queue = newq
            is_even = not is_even
        return True
