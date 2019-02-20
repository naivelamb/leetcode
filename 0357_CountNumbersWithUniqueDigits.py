# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/count-numbers-with-unique-digits/

Let f(k) be the number of numbers with unique digits with 0

Then we know,
f(1) = 10
f(2) = 9 * 9
f(3) = 9 * 9 * 8
f(k) = f(k - 1) * (9 - k + 2)

Let s(n) be the answer for n, then
s(n) = s(n - 1) + f(n)

If n > 10, return s(min(n, 10))
Time complexity O(1)
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: 'int') -> 'int':
        f = [0] * 11 # count of number of k-digit
        for i in range(1, 11):
            if i == 1:
                f[i] = 10
            elif i == 2:
                f[i] = 9 * 9
            else:
                f[i] = f[i - 1] * (9 - i + 2)
        s = [0] * 11 # answer for number of k-digit
        for i in range(1, 11):
            s[i] = s[i-1] + f[i]
        if n <= 0: return 1
        return s[min(n, 10)]
        