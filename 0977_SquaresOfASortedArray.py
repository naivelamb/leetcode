# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/squares-of-a-sorted-array/

Split the array into two parts: 
Smaller: all < 0
Larger: all >= 0
Get square of both part, reverse the smaller. Then merge two arrays.
"""
class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # Special cases: all >= 0 and all <= 0
        if A[0] >= 0:
            return [x**2 for x in A]
        if A[-1] <= 0:
            return [x**2 for x in A[::-1]]
        
        # Split the array
        smaller, larger = [], []
        for x in A:
            if x >= 0:
                larger.append(x**2)
            else:
                smaller.append(x**2)
        smaller = smaller[::-1]
        
        # Merge
        ans = []
        i, j = 0, 0
        while i < len(smaller) and j < len(larger):
            if smaller[i] > larger[j]:
                ans.append(larger[j])
                j += 1
            else:
                ans.append(smaller[i])
                i += 1
        ans += smaller[i:] + larger[j:]
        return ans
        
        
