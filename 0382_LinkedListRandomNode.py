# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/linked-list-random-node/submissions/

Reservoir sampling. 

Time complexity: getRandom: O(n)
"""
import random
class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        res, node, idx = self.head, self.head.next, 1
        while node:
            if random.randint(0, idx) == 0:
                res = node
            node = node.next
            idx += 1
        return res.val

