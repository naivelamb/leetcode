# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

#1 Convert to array, then build recursively. O(n)
#2 Find mid, cut, then build recursively. O(nlogn)
#3 Control left and right boundary. 
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST_list(self, head: 'ListNode') -> 'TreeNode':
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        def helper(vals):
            if not vals:
                return None
            mid = len(vals) // 2
            root = TreeNode(vals[mid])
            left = helper(vals[:mid])
            right = helper(vals[mid + 1:])
            root.left = left
            root.right = right
            return root
        return helper(vals)
    
    def sortedListToBST_cut(self, head: 'ListNode') -> 'TreeNode':
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        mid = slow
        prev.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST_cut(head)
        root.right = self.sortedListToBST_cut(mid.next)
        return root
    
    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        n = self.getSize(head)
        self.head = head
        
        def build(l, r):
            if l > r:
                return None
            
            mid = (l + r) // 2
            left = build(l, mid - 1)
            node = TreeNode(self.head.val)
            node.left = left
            self.head = self.head.next
            node.right = build(mid + 1, r)
            return node
        
        return build(0, n - 1)
        
    def getSize(self, head):
        n, curr = 0, head
        while curr:
            n += 1
            curr = curr.next
        return n