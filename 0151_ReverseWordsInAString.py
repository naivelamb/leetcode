# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/reverse-words-in-a-string/

Split then reverse
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        res = []
        for x in s:
            if x:
                res.append(x)
        return ' '.join(res[::-1])
