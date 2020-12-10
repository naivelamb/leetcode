"""
https://leetcode.com/problems/binary-search-tree-iterator/

Go all the way to the most left nodes, and use a stack to store the nodes we go through. 

When call next, pop the last node from the stack, go to its right, and keep append left sub-nodes to the stack.

__init__: O(h)
hasNext: O(1)
next: at most O(h)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        node = self.stack.pop()
        val = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return val

    def hasNext(self) -> bool:
        if self.stack:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()