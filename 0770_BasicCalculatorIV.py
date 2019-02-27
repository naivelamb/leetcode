# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/basic-calculator-iv/

We store the result in the form of dictionary. 
2*a + 3*b + 5*a*b=> {('a'): 2, ('b'): 3, ('a', 'b'): 5}
We need to define a compute method, giving it 'left', 'right', and 'op', it 
will return the result polynominal.
The evalvars and evalints can be initiated as a dinctionary, and all evalvars
can be replaced. 
Expression need to be splitted, this can be done by regular expression. 
The polynomials will be stored in a stack, ops will be stored in another one. 
During the scan, we compute the result inside any parentheses. What's more, if
we see an operator that has lower priority than the previous operator, we need 
to compute. For example, the last operator is '*', now we see a '+' or '-'.
At the end, we just pop the stack to get the final result.
"""
import re
class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        ref_val = {n:v for n, v in zip(evalvars, evalints)}
        stack, ops = [], []
        priority = {'(': 0, '+': 1, '-': 1, '*': 2}
        for t in re.findall(r'\(|\)|[a-z]+|[0-9]+|[\+\-\*]', expression):
            if t[0].isdigit():
                stack.append({tuple():int(t)})
            elif t[0].isalpha():
                if t in ref_val:
                    stack.append({tuple():int(ref_val[t])})
                else:
                    stack.append({tuple([t,]): 1})
            elif t == '(':
                ops.append('(')
            elif t == ')':
                # end of a parentheses, compute
                while ops and ops[-1] != '(':
                    stack.append(self.compute(stack.pop(-2), stack.pop(-1), ops.pop()))
                ops.pop()
            elif t in '+-*':
                if not ops or priority[t] > priority[ops[-1]]:
                    ops.append(t)
                else:
                    while ops and priority[t] <= priority[ops[-1]]:
                        stack.append(self.compute(stack.pop(-2), stack.pop(-1), ops.pop()))
                    ops.append(t)
        while ops: # what is left should be only '+' and '-'
            stack.append(self.compute(stack.pop(-2), stack.pop(-1), ops.pop()))
        
        # build the result
        res = []
        for k in sorted(stack[0], key = lambda x: (-len(x), x)):
            v = stack[0][k]
            if v != 0:
                if not k:
                    res.append(str(v))
                else:
                    res.append('%s*%s' % (v, '*'.join(k)))
        return res
    
    def compute(self, left, right, op):
        # left, right => dictionary for left and right part of an operator
        if op == '+':
            for k in right:
                left[k] = left.get(k, 0) + right[k]
            return left
        if op == '-':
            for k in right:
                left[k] = left.get(k, 0) - right[k]
            return left
        if op == '*':
            ans = {}
            for k1 in left:
                for k2 in right:
                    v1, v2 = left[k1], right[k2]
                    newk = tuple(sorted(k1 + k2))
                    ans[newk] = ans.get(newk, 0) + v1 * v2
            return ans