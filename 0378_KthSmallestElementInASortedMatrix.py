# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

#1 Heap
We can use the first remaining element in each row to represent this row, which is the head of each row initially. Every time we heappop an element, we need to make sure either:
	1. All the elements in this row have been in the heap once.
	2. Next element is used as 'head' to represent this row. 
This means we need to check if there is anything left, if so we need to push one element to the heap. 
The heap is always of size n, it will give us time complexity O(n + k log(n)). 

#2 Heap + BFS
heap = [(matrix[i][j], i, j)]
when j == 0, add (i + 1, j)
add (i, j + 1)
Untill find k. 

Time Complexity: O(klogk)
"""
import heapq
class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        heap = [(matrix[0][0], 0, 0)]
        cnt, n = 0, len(matrix)
        while cnt < k and heap:
            val, i, j = heapq.heappop(heap)
            cnt += 1
            if cnt == k:
                return val
            if i + 1 < n and j == 0:
                heapq.heappush(heap, (matrix[i+1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j+1], i, j + 1))
        return
    
    def kthSmallest_vanilaHeap(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(n)]
        
        ans = 0
        for _ in range(k):
            ans, i, j = heapq.heappop(heap)
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ans
            