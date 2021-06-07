class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def largetSubtreeSum(self, root):
        self.ans = float('-inf')
        def subtreeSum(node):
            if node.left:
                left = subtreeSum(node.left)
            else:
                left = 0
            if node.right:
                right = subtreeSum(node.right)
            else:
                right = 0
            self.ans = max(self.ans, node.val + left + right)
            return node.val + left + right

        subtreeSum(root)
        return self.ans

root = TreeNode(1) 
root.left = TreeNode(-2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.right.left = TreeNode(-6) 
root.right.right = TreeNode(2)

s = Solution()
print(s.largetSubtreeSum(root))