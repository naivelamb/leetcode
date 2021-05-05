"""
https://leetcode.com/problems/partition-list/

2 pointer. Create two dummy linked list to store (<x) and (>=x) respectively.

Time compleixty: O(N)
"""
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = l1 = ListNode(0) # < x
        dummy2 = l2 = ListNode(0) # >= x
        curr = head
        while curr:
            tmp = curr.next
            curr.next = None
            if curr.val < x:
                l1.next = curr
                l1 = curr
            else:
                l2.next = curr
                l2 = curr
            curr = tmp
        l1.next = dummy2.next
        return dummy1.next