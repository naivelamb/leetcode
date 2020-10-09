"""
https://leetcode.com/problems/serialize-and-deserialize-bst/

All trees need two of pre/in/post order traverse results to rebuild it. Since the in-order traverse of BST is an non-decreasing order, we can build a pre-order traverse and then rebuild it.

Time complexity: O(N) for both serialize and deserialize.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        vals = []
        def pre_order(root):
            if root:
                vals.append(root.val)
                pre_order(root.left)
                pre_order(root.right)
        pre_order(root)
        vals = map(str, vals)
        return ','.join(vals)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return 
        vals = data.split(',')
        vals = map(int, vals)
        vals = collections.deque(vals)
        def build(min_val, max_val):
            if vals and min_val < vals[0] < max_val:
                node = TreeNode(vals.popleft())
                node.left = build(min_val, node.val)
                node.right = build(node.val, max_val)
                return node

        root = build(-float('inf'), float('inf'))
        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
