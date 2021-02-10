"""
https://leetcode.com/problems/copy-list-with-random-pointer/
Use a hash map to store the relation between old node and new node, then deep copy the linked list.
Time complexity: O(N)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        ref, prev, node = {}, None, head
        while node:
            if node not in ref:
                ref[node] = Node(node.val, node.next, node.random)
            if prev:
                prev.next = ref[node]
            else:
                head = ref[node]
            if node.random:
                if node.random not in ref:
                    ref[node.random] = Node(node.random.val, node.random.next, node.random.random)
                ref[node].random = ref[node.random]
            prev, node = ref[node], node.next

        return head