# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/merge-sorted-array/

Scan from the back
"""
class Solution:
    def merge(self, nums1: 'List[int]', m: 'int', nums2: 'List[int]', n: 'int') -> 'None':
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        print(nums1)
        
s = Solution()
n1 = [2, 2, 3, 0, 0, 0]
n2 = [1, 1, 1]
s.merge(n1, 3, n2, 3)
