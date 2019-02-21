# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/multiply-strings/

multiply and add by digit

Time Complexity: O(m + n)
"""
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        for i, v1 in enumerate(num1[::-1]):
            for j, v2 in enumerate(num2[::-1]):
                int1 = ord(v1) - ord('0')
                int2 = ord(v2) - ord('0')
                res[i + j] += int1 * int2
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        while res and res[-1] == 0:
            res.pop()
        return ''.join(map(str, res[::-1]))

s = Solution()
print(s.multiply('123', '456'))