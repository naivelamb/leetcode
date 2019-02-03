# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/sum-of-even-numbers-after-queries/

Go through A, get the sum of even numbers. 
Then do the queries, 
Old_a is odd, new_a is even => add new_a to total.
Old_a is even, new_a is odd => minus old_a from total
Old_a is even, new_a is even, => add val to total

Time Complexity: O(m + n), m = len(A), n = len(queries)
"""
class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        ans = []
        total = 0
        for a in A:
            if a % 2 == 0:
                total += a
        for val, idx in queries:
            old_a = A[idx]
            A[idx] += val
            new_a = A[idx]
            # old_a is odd
            if old_a % 2 != 0:
                if new_a % 2 == 0:
                    total += new_a
            # old_a is even
            else:
                if new_a % 2 == 0:
                    total += val
                else:
                    total -= old_a
            ans.append(total)
        return ans
