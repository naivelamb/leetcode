# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Do it digit by digit
"""
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ref = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        res = []
        for digit in digits:
            choices = ref[ord(digit) - ord('2')]
            if not res:
                res = choices
            else:
                tmp = []
                for prev in res:
                    for c in choices:
                        tmp.append(prev + c)
                res = tmp
        return res
    
    def letterCombinations_backtrack(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ref = {'2': 'abc', 
           '3': 'def', 
           '4': 'ghi',
           '5': 'jkl',
           '6': 'mno',
           '7': 'pqrs',
           '8': 'tuv',
           '9': 'wxyz'}
        
        res = []
        
        def dfs(curr, next_digits):
            if not next_digits:
                res.append(curr)
            else:
                for letter in ref[next_digits[0]]:
                    dfs(curr + letter, next_digits[1:])
        if digits:
            dfs('', digits)
        return res
