# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/string-compression/

Two-pointer.

Time complexity: O(n)
"""
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left = i = 0
        while i < len(chars):
            ch, length = chars[i], 1
            while (i + 1) < len(chars) and ch == chars[i + 1]:
                length += 1
                i += 1
            chars[left] = ch
            if length > 1:
                str_len = str(length)
                chars[left + 1: left + 1 + len(str_len)] = str_len
                left += len(str_len)
            left += 1
            i += 1
        return left