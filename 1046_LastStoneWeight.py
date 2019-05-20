# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/last-stone-weight/

Use heap to store the stones, pop biggest two every step. 

Time Complexity: O(nlogn), n -> len(stones)
"""
import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y - x)
        return heap[0] if heap else 0
                