"""
https://leetcode.com/problems/reverse-linked-list-ii/

Find front and end, and reverse middle part.

Time complexity: O(N)
"""
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right: # no reverse
            return head
        
        prev = None
        curr = head
        i = 1

        while i <= right:
            if i == left:
                front = prev
                start = curr
            if i == right:
                end = curr
                tail = curr.next
            if left <= i <= right: # reverse
                next_tmp = curr.next
                curr.next, prev = prev, curr
                curr = next_tmp
            else:
                prev, curr = curr, curr.next
            i += 1
        
        if front == None: # reverse from head
            start.next = tail
            return end

        front.next = end
        start.next = tail
        return head