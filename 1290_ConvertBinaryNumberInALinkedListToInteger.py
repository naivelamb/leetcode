"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

ans = ans * 2 + node.val
node = node.next

Time complexity: O(N)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans