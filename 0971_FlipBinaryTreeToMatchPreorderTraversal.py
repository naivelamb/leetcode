"""
https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

Let's say we have a pointer for the voyage. We can only proceed if voyage[pointer] == curr_node.val. 
Then we need to check the left child of the node and next pointer, if they are not the same, we try to swap and then check again. If not satisified, we cannot meet the requirement by swap.
If we can meet, then keep doing this. ==> recurssion. 

dfs(root) -> return if we can flip the binary tree to match the prorder traversal. 
need a self.next as pointer. 

Time complexity: O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def dfs(root):
            if not root:
                return True
            if root.val != voyage[self.next]:
                return False
            self.next += 1
            if root.left and root.right and root.left.val != voyage[self.next]:
                res.append(root.val)
                root.left, root.right = root.right, root.left
            return dfs(root.left) and dfs(root.right)
        
        self.next, res = 0, []
        if dfs(root):
            return res
        else:
            return [-1]