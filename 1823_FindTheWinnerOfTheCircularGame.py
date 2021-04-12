"""
https://leetcode.com/problems/find-the-winner-of-the-circular-game/

Double linked list
Time complexity: O(NK)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.prev = None

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        
        for i in range(n):
            if i == 0:
                head = ListNode(i + 1)
                curr = head
            elif i == n - 1:
                node = ListNode(i + 1)
                curr.next = node
                node.prev = curr
                node.next = head
                head.prev = node
            else:
                node = ListNode(i + 1)
                curr.next = node
                node.prev = curr
                curr = curr.next
        
        curr = head
        while curr.next.val != curr.val:
            for _ in range(k-1):
                curr = curr.next
            tmp = curr.next
            curr.prev.next, curr.next.prev = curr.next, curr.prev
            curr = tmp
        return curr.val
                