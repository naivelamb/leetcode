# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/super-ugly-number/

Ugly number can only be generated from the multiplications between the provided
primes. 

The 1st ugly number is always 1, and the candidates are primes (prime x 1). 
We pick the smallest one from the candidates as the 2nd ugly number. 
Now the corresponding number should be updated by multiplying the next ugly
number.

Example: primes = [2, 7, 13, 19]

n = 1, ugly_nums = [1], candidates = [2, 7, 13, 19]
n = 2, ugly_nums = [1, 2], candidates = [4(2x2), 7, 13, 19]
n = 3, ugly_nums = [1, 2, 4], candidates = [8(2x4), 7, 13, 19]
n = 4, ugly_nums = [1, 2, 4, 7], candidates = [8, 14(7x2), 13, 19]
n = 5, ugly_nums = [1, 2, 4, 7, 8], candidates = [14(2x7), 14, 13, 19]
n = 6, ugly_nums = [1, 2, 4, 7, 8, 13], candidates = [14, 14, 26(13x2), 19]
n = 7, ugly_nums = [1, 2, 4, 7, 8, 13, 14], candidates = [16(2x8), 28(7x4), 26, 19]

A pointer array is used to keep track of multiplying which ugly number to the 
corresponding prime when update. 
=> candidates[i] = ugly_nums[pointer[i]] * primes[i]

We need to do this from n = 1 to n = n. 

Time complexity is O(nk), where k = len(primes)
"""
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly_nums = [1]
        k = len(primes)
        pointer = [0]*k
        candidates = primes[:]
        
        for _ in range(1, n):
            # get the next ugly number
            next_ugly_num = min(candidates)
            ugly_nums.append(next_ugly_num)
            # update the candidate
            for i in range(k):
                if candidates[i] == next_ugly_num:
                    pointer[i] += 1
                    candidates[i] = primes[i] * ugly_nums[pointer[i]]
        return ugly_nums[-1]

