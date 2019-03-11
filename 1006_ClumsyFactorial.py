# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/clumsy-factorial/

N = 5: 5*4/3 + 2 - 1
N = 9: 9*8/7 + 6 - 5*4/3 + 2 - 1

So for each N, we need to break the result into two parts:
    before '+' and after '+'
Then we can solve it by recursion. 
first, second = helper(N - 4)
new_first = N * (N - 1) // (N - 2)
new_second = N - 3 - first + second

Time Complexity: O(N)
"""
class Solution:
    def clumsy(self, N: int) -> int:
        def helper(N):
            if N == 1:
                return 1, 0
            if N == 2:
                return 2, 0
            if N == 3:
                return 6, 0
            if N == 4:
                return 4*3//2, 1
            if N == 5:
                return 5*4//3, 1
            a, b = helper(N - 4)
            new_a = N * (N - 1) // (N - 2)
            new_b = (N - 3) - a + b
            return new_a, new_b
        return sum(helper(N))