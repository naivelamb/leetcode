# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

#1 Brute force:
Generate all pairs, put into a heap, then pop. O(m*n)

#2 Use heap. 
Initialize the heap as (nums1[i] + nums2[0], i, 0). 
Every time pop one element from heap, we push a new element which is,
(nums1[i] + nums2[j + 1], i, j+1) to the heap. 

Time Complexity: O(m + klogm)

#3 BFS
The pairs of [1, 7, 11] and [2, 4, 6] can be viewed as a matrix:
   |  1  |   7  |  11   
2  |  3  |   9  |  13
4  |  5  |  11  |  15
6  |  7  |  13  |  17
We can do BFS from the top-left corner, expand to the right and bottom cell. 

O(klogk)
"""
import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) * len(nums2) <= k:
            return [[n1, n2] for n1 in nums1 for n2 in nums2]
        res, n, cnt = [], len(nums2), 0
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        while heap and cnt < k:
            cnt += 1
            total, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j < n - 1:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
    
    def kSmallestPairs_bfs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        heap = [(nums1[0] + nums2[0], 0, 0)]
        res, cnt, seen = [], 0, {}
        seen[0, 0] = 1
        while cnt < k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            cnt += 1
            if i + 1 < len(nums1) and j == 0:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
                seen[i + 1, j] = 1
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                seen[i, j + 1] = 1
        return res