# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/h-index/

#1 Sort, then check from the most cited paper.
H = 0, if # of cite > H, H += 1
Else return H.
At the end, return H. 
Time Complexity: O(nlogn)

#2 O(n) solution based on count. 
The possilbe h index values are [0, 1, 2, ..., n], n = # of papers.
So we record the count of papers for each citations, if a paper's citations is 
more than n, we put it at the end. 
Then we just need to count how many papers have citations >= a citation. 
Do it from the most possilbe citations. 

"""
class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        citations.sort()
        h = 0
        for citation in citations[::-1]:
            if citation > h:
                h += 1
            else:
                return h
        return h
    
    def hIndex_count(self, citations: 'List[int]') -> 'int':
        n = len(citations)
        count = [0] * (n+1)
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        
        i = n - 1
        while i >= 0:
            count[i] += count[i+1]
            if count[i+1] >= i + 1:
                return i + 1
            i -= 1
        return 0
        
s = Solution()
a = [0]
print('Should be 0. The answer is: ', s.hIndex(a))
a = [3,0,6,1,5]
print('Should be 3. The answer is: ', s.hIndex(a))

a = [0]
print('Should be 0. The answer is: ', s.hIndex_count(a))
a = [3,0,6,1,5]
print('Should be 3. The answer is: ', s.hIndex_count(a))