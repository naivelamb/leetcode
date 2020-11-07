"""
https://leetcode.com/problems/add-two-numbers-ii/

Record and add, or reverse the linked list are trivial. 

We use stack to record the values, when we pop the stack, we naturally go from right to left. 
As long as we know the current node, we can easily link it to its "previous" node, since the next pop would be its "previous" node. 

Time complexity: O(m+n)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry, dummy = 0, None
        while stack1 or stack2:
            total = carry
            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()
            
            carry = total // 10
            total %= 10

            dummy = ListNode(total, dummy)

        if carry != 0:
            dummy = ListNode(1, dummy)

        return dummy