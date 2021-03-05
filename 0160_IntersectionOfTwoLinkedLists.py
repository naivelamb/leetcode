"""
https://leetcode.com/problems/intersection-of-two-linked-lists/

Get the length of A and B, lA, lB. delta = abs(lA - lB).
If lA > lB, move lA delta step first, vice versa. 

This would guarentee find the intersection. 

Time complexity: O(N)
Space complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p, la = headA, 0
        while p:
            p = p.next
            la += 1
        p, lb = headB, 0
        while p:
            p = p.next
            lb += 1
        delta = abs(la - lb)
        pa, pb = headA, headB
        if la > lb:
            while delta != 0:
                pa = pa.next
                delta -= 1
        elif lb > la:
            while delta != 0:
                pb = pb.next
                delta -= 1
        
        while pa and pb:
            if pa == pb:
                return pa
            else:
                pa = pa.next
                pb = pb.next
        
        return None   