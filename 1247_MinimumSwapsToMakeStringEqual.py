# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

Two types of mismatch:
1) x in s1, y in s2;
2) y in s1, x in s2.

We need one swap to make two type-1 mismatch match;
We need two swap to make a type-1 and a type-2 mismatch match.

So we only need to count the number of different mismatch.
If (n1 + n2) % 2 == 1, we cannot swap to make two string equal.

Time complexity: O(n)
"""

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        n1, n2 = 0, 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    n1 += 1
                else:
                    n2 += 1

        if (n1 + n2) % 2 == 1:
            return -1
        else:
            return (n1//2 + n2//2 + 2*(n1%2))

sol = Solution()

s1 = 'xx'
s2 = 'yy'
assert sol.minimumSwap(s1, s2) == 1

s1 = 'xy'
s2 = 'yx'
assert sol.minimumSwap(s1, s2) == 2

s1 = 'xx'
s2 = 'xy'
assert sol.minimumSwap(s1, s2) == -1

s1 = "xxyyxyxyxx"
s2 = "xyyxyxxxyx"
assert sol.minimumSwap(s1, s2) == 4
