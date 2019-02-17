# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

Greedy. We do K flip from the most left '0'.
Let's say A[i] == 0 and it’s the most left '0'.
If we start flipping from j, where j < i, this means we flipped a '1' to '0'. 
Eventually we have to flip it again, meaning we do two flips for it, which is 
not optimal.
If we start flipping from j, where j > i, making A[j] -> 1. Let's assume 
j - i < K. Eventually we have to flip A[i], which will flip A[j] back to 0, 
indicating we have to do at least one more flip, which is not optimal. 
Therefore, we have to flip starting from A[i].

If we simulate this process, we can easily get an O(NK) solution, which is a TLE. 

So we need to find an O(1) to keep the information about flip. We can do this 
by remember the current flips for the i-th index. 
If curr_flips is odd and A[i] == 1, we need to flip it.
If curr_flips is even and A[i] == 0, we need to flip it. 

Since we only move forward, we can store curr_flips into A[i] once we finish 
flip A[i]. But we need to avoid the case when A[i] == 1 and it is not flipped. 

Therefore, after flip A[i] we will set A[i] = 2, and when we see (i > K), 
curr -= A[i-K] // 2
"""

class Solution:
    def minKBitFlips(self, A: 'List[int]', K: 'int') -> 'int':
        cur = res = 0
        for i in range(len(A)):
            if i >= K:
                cur -= A[i - K] // 2
            if A[i] == cur % 2:
                if i + K > len(A):
                    return -1
                A[i] = 2
                cur, res = cur + 1, res + 1 
        return res
    
s = Solution()
A = [0,1,0,0,0,0,1,1,0,1,0,0,0,0,1,1,1,0,1,1]
K = 5
print(s.minKBitFlips(A, K))
#A = [1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,1,1]
#K = 8
#print(s.minKBitFlips(A, K))
