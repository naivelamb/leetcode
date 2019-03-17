# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/numbers-with-1-repeated-digit/

Let cnt_non_dup be the count of the non-duplicate numbers smaller than N.
Then the answer is N - cnt_non_dup.

For all k-digit numbers, we know the count of non-duplicate numbers are
9 * A(9, k - 1), where A is the permutation. 

So for N, let's assume it is k digit, we can easily compute count of 
non-duplicate numbers for (1,2,3,4,k-1) digit. Then we need to compute the 
non-duplicate numbers in the range [10^(k - 1), N]

We first compute N to a list of integers. Take 25654 as an example.
We first look for numbers like 1xxxx, the result is A(9, 4)
Next, look for numbers like 2(0-4)xxx, the result is 5 * A(8, 3), but 2 is used,
so we only have 4 * A(8, 3)
Next, look for numbers like 25(0-5)xx, the result is 6 * A(7, 2), but 2 and 5 
are used, so we only have 4 * A(7, 2)
Next, look for numbers like 256(0-4)x, the result is 5 * A(6, 1), but 2 is used,
so we only have 4 * A(6, 1)

Therefore, assume we have x at i-th digit, then the numbers smaller than N by change
the (i + 1) to the last digits are A(9 - i, k - i - 1) times the number of number 
not used in the range of [0, x). 

Need to be careful about the first digit, it cannot be 0. 
"""
class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        L = list(map(int, str(N)))
        res, n = 0, len(L)
        
        def A(m, n):
            # permutation
            if n == 0:
                return 1
            else:
                return A(m, n - 1) * (m - n + 1)
        
        # compute count of non-duplicate numbers for n < 10^(k - 1)
        for i in range(1, n):
            res += 9 * A(9, i - 1)
        
        s = set()
        for i, x in enumerate(L):
            # if i == 0, then range is (1, x) else it is (0, x)
            for y in range(0 if i else 1, x):
                if y not in s:
                    res += A(9 - i, n - i - 1)
            if x in s:
                break
            s.add(x)
        return N - res
            
