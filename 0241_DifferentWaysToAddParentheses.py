# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:06:33 2019

For an operator at index i, we can first compute the possible results by adding
parentheses for the first part input[:i], as well as the second part input[i+1:].
Then the answer is just all the possible combinations of number in the first part
 and number in the second part, using the operator input[i]. 
"""
import collections
class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in '+-*':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for a in res1:
                    for b in res2:
                        res.append(self.helper(a, b, input[i]))
        return res
    
    def helper(self, m, n, op):
        if op == '+':
            return m + n
        if op == '-':
            return m - n
        if op == '*':
            return m * n
        
    
s = Solution()
a = '15*1*4'
print(s.diffWaysToCompute(a))
