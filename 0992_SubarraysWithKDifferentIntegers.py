# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/subarrays-with-k-different-integers/

If we know f(K) => subarrays with number of different integers at most K, then 
the answer is 
f(K) - f(K - 1).

f(K) can be solved using sliding window. 
"""
import collections
class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        return self.atMostK(A, K) - self.atMostK(A, K - 1)
    
    def atMostK(self, A, K):
        cnt = collections.Counter()
        res, i = 0, 0
        for j in range(len(A)):
            if cnt[A[j]] == 0:
                K -= 1
            cnt[A[j]] += 1
            while K < 0:
                cnt[A[i]] -= 1
                if cnt[A[i]] == 0:
                    K += 1
                i += 1
            res += j - i + 1
        return res
A = [1,2,1,3,4]
K = 3
s = Solution()
print(s.subarraysWithKDistinct(A, K))