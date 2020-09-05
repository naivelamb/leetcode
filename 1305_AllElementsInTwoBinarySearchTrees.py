"""
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
#1 Traverse root1 & roo2, get the sorted list, then merge.
Time Complexity: O(2(m+n))

#2 One-pass
Traverse the two tree together, output the results.
Time Complexity: O(m+n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        l1, l2 = inorder(root1), inorder(root2)
        ans = []
        p1, p2 = 0, 0
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] < l2[p2]:
                ans.append(l1[p1])
                p1 += 1
            else:
                ans.append(l2[p2])
                p2 += 1
        if p1 < len(l1):
            ans += l1[p1:]
        if p2 < len(l2):
            ans += l2[p2:]
        return ans

    def getAllElements_1pass(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, ans = [], [], []
        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                ans.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                ans.append(root2.val)
                root2 = root2.right
        return ans
