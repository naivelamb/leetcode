# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/merge-k-sorted-lists/

Need a helper function to merge 2 list
Then we just keep doing it. 

Time Complexity: Nlogk
N -> total nodes
k -> total list
"""
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        jump = 1
        while jump < n:
            for i in range(0, n - jump, jump * 2):
                lists[i] = self.mergeTwoList(lists[i], lists[i + jump])
            jump *= 2
        return lists[0] if n > 0 else lists
        
    
    def mergeTwoList(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val > l2.val:
            head = l2
            l2.next = self.mergeTwoList(l1, l2.next)
        else:
            head = l1
            l1.next = self.mergeTwoList(l1.next, l2)
        return head
