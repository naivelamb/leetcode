# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/palindrome-permutation/

Check the char counts. At most one odd count.
"""
class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ref = {}
        for c in s:
            ref[c] = ref.get(c, 0) + 1
        
        odd = 0
        for c in ref:
            if ref[c] % 2:
                odd += 1
                if odd > 1:
                    return False
        return True
