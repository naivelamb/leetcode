"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Two pointers
p1 -> last non-duplicate node
p2 -> current node 

if p2.val != p2.next.val, move p1 and p2 forward together. 
else only move p2

Time complexity: O(N)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = pre = ListNode()
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next