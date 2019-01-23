# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/linked-list-cycle-ii/

Let's assume we have F points outside the circle, C points in the circle. 
Slow and Fast pointer starts from head, moves at 1-step and 2-step a time 
respectively. 

After k moves, they meet the h-th point, therefore, we know
h == (k - F) % C == (2k - F) % C

In other words,
k = C * m + F + h
2k = C * n + F + h

Therefore, k = C * (n - m) => k % C == 0

h + F = (n - 2m) * C

Let's take n = 1 (the first time the two pointers meet), then m = 0 => h + F = C.
Therefore, after two pointer meet, we put one pointer back to head. Then set 
the speed as 1-step a time, they will meet again at the starting node. 

Time: O(n), space: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Space O(n) solution using set. 
        """
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return curr
            else:
                visited.add(curr)
                curr = curr.next
        return None
        
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        intersect = self.getIntersect(head)
        if intersect is None:
            return None
        
        pt1, pt2 = head, intersect
        while pt1 != pt2:
            pt1 = pt1.next
            pt2 = pt2.next
        return pt1
        
    def getIntersect(self, head):
        # return the meeting point in the circle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

