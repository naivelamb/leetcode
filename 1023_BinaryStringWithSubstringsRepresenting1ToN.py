# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

Let m = len(S). We can find all the numbers that can be formed by the substrings
of S. => O(m^2)

Then we heapify the number array, check whether the array contains all the numbers
from 1 to N. 

Time complexity: O(m^2) + O(NlogN)
"""
import heapq
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        vals = set()
        n = len(S)
        for i in range(n):
            if S[i] == 0:
                continue
            for j in range(i+1, n + 1):
                val = int(S[i:j], 2)
                if val not in vals:
                    vals.add(val)
        heap = list(vals)
        heapq.heapify(heap)
        heapq.heappop(heap) # pop 0
        if len(heap) < N:
            return False
        for i in range(1, N + 1):
            if i == heapq.heappop(heap):
                continue
            else:
                return False
        return True
                
