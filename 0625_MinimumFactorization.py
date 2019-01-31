# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/minimum-factorization/

If x < 10, return x.
Else, the number must be able to be expressed as:
Num = 9^x9 + 8^x8 + 7^x7 + 6^x6 + 5^x5 + 4^x4 + 3^x3+2^x2
Otherwise return 0
Then the answer is simply,
Sum(x_i * 'i') for all x_i != 0, i in increasing order. 

We solve the problem in a greedy way. Start dividing the number by 9, 8, 7 … We only proceed to next divider if the number is not divisible by current divider. 
Meanwhile, we can assemble the answer using string expression, and return the reversed string. 

32-bit signed integer -> the answer should be in range[-2^31, 2^31 - 1]

Time complexity is O(n), where n = sum(x_i).
"""
class Solution:
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        dividers = [9, 8, 7, 6, 5, 4, 3, 2]
        if a < 10:
            return a
        ans = ''
        for divider in dividers:
            while a % divider == 0:
                ans += str(divider)
                a //= divider
        ans = int(ans[::-1]) if ans else 0
        if a > 1 or ans >= 2**31:
            return 0
        else:
            return ans
