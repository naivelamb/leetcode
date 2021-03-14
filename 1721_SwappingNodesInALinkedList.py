"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

Linked list -> array -> swap -> rebuild linked list
Time complexity: O(N)
Space complexity: O(N)

Find the two node and the corresponding pre/next, swap. 
Time complexity: O(N)
Space comlexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        curr, n = dummy, 0
        while curr.next:
            if n == k - 1:
                prev1 = curr
                node1 = curr.next
            curr = curr.next
            n += 1

        curr, i = dummy, 0
        while i != n - k + 1:
            if i == n - k:
                prev2 = curr
                node2 = curr.next
            curr = curr.next
            i += 1

        # swap
        prev1.next = node2
        prev2.next = node1
        node1.next, node2.next = node2.next, node1.next
        return dummy.next