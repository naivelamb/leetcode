# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

Find kth element recursively
Time Complexity: O(log(m + n))
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.findkth(nums1, nums2, l//2)
        else:
            return (self.findkth(nums1, nums2, l//2) + self.findkth(nums1, nums2, l//2-1))/2
        
        
    def findkth(self, A, B, k):
        m, n = len(A), len(B)
        if m > n:
            A, B = B, A
            m, n = n, m
        if not A:
            return B[k]
        if k == 0:
            return min(A[0], B[0])
        if k == m + n -1 :
            return max(A[-1], B[-1])
        
        i = m // 2
        j = k - i
        if A[i] < B[j]:# A[:i], (A[i:], B[:j]), B[j:]
            return self.findkth(A[i:], B[:j], j)
        else: # B[:j], (A[:i], B[j:]), A[i:]
            return self.findkth(A[:i], B[j:], i)