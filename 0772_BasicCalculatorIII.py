# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/basic-calculator-iii/

Need a helper method that do the compute.
Scan the expression, we need to remember the last operators -> op and current num.
When we see '(', it is the start of another expression. We put previous op to
the stack and initialize num = 0, op = '+'. 
When we see '+-*/', it means we finish wrap up a num, we need to compute the
result. Now, num = 0, op = new_op.
When we see ')', it is the end of an expression. We need to keep compute until 
stack gives an operator. 
"""
class Solution:    
    def calculate(self, s: str) -> int:
        def compute(op, num):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop()*num)
            elif op == '/':
                stack.append(int(stack.pop()/num))
        
        num, op = 0, '+'
        stack = []
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in '+-*/':
                compute(op, num)
                num, op = 0, ch
            elif ch == '(':
                stack.append(op)
                num, op = 0, '+'
            elif ch == ')':
                compute(op, num)
                num = 0
                while isinstance(stack[-1], int):
                    num += stack.pop()
                op = stack.pop()
                compute(op, num)
                num, op = 0, ch
        compute(op, num)
        return sum(stack)