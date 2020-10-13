"""
https://leetcode.com/problems/sort-list/

Divide and conquer. Find the mid of the linked liked list, cut, then sort the two sublist then merge.

Time complexity: O(NlogN)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow = slow, slow.next
            fast = fast.next.next
        pre.next = None

        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, h1, h2):
        dummy = ListNode(None)
        curr = dummy
        while h1 and h2:
            if h1.val < h2.val:
                curr.next = h1
                curr = curr.next
                h1 = h1.next
            else:
                curr.next = h2
                curr = curr.next
                h2 = h2.next

        curr.next = h1 or h2

        return dummy.next
