"""
https://leetcode.com/problems/insertion-sort-list/

Insert a given value to a "sorted linked list", keep doing this for all nodes.

Time complexity: O(N^2)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        pseudo_head = ListNode()
        
        curr = head #pointer to the node we are dealing with
        while curr:
            prev_node = pseudo_head
            next_node = pseudo_head.next
            while next_node: # find location
                if curr.val < next_node.val:
                    break
                prev_node = next_node
                next_node = next_node.next
                
            next_iter = curr.next
            curr.next = next_node
            prev_node.next = curr
            
            curr = next_iter
        return pseudo_head.next