# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/linked-list-cycle/

Two pointer: slow -> moves 1 step a time; fast -> moves 2 step a time. 
If there is loop, then slow will meest. 
Else, fast will reach None. 

Time: O(n), Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Space O(n) solution using Set. 
        """
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            else:
                seen.add(curr)
                curr = curr.next
        return False
    
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True