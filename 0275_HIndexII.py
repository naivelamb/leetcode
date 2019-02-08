# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/h-index-ii/

Binary search O(nlogn)

Citations[mid] == len - mid, there are mid papers that have at least 
citations[mid] citations.

Citations[mid] > len - mid, there are mid papers that have more than 
citations[mid] citations, search in the left half.

Citations[mid] < len - mid, there are mid papers that have less than 
citations[mid] citations, search in the right half. 
"""
class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        n = len(citations)
        l, r = 0, n-1
        while l <= r:
            mid = (l + r)//2
            if citations[mid] >= n - mid:
                r = mid - 1
            else:
                l = mid + 1
        return n - l
    
s = Solution()
a = [0]
print('Should be 0. The answer is: ', s.hIndex(a))
a = [3,0,6,1,5]
print('Should be 3. The answer is: ', s.hIndex(a))