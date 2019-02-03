# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/number-of-atoms/

When we see a '(', we need to parse the string to get the count of each atom. 
When we see a ')', we need to get the count of the atoms in the parentheses, and multiply the count to the previous count. 

So we use a stack of dictionary to record the count in each parentheses, and go from the inside to outside.

Be careful about:
	1. Account for lower string when extract atom name.
	2. If there is only 1 atom, then 1 is not shown in the expression. This applies to both single atom and a group of atoms. 
Time Complexity: O(n^2)
"""
class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        N = len(formula)
        stack = [{}]
        i = 0
        while i < N:
            # find a new group of atoms
            if formula[i] == '(':
                stack.append({})
                i += 1
            # end of a group of atoms
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < N and formula[i].isdigit():
                    i += 1
                cnt = int(formula[i_start: i] or 1)
                for atom in top:
                    stack[-1][atom] = stack[-1].get(atom, 0) + top[atom] * cnt
            # parse a group of atoms
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower():
                    i += 1
                atom = formula[i_start: i]
                i_start = i
                while i < N and formula[i].isdigit():
                    i += 1
                cnt = int(formula[i_start: i] or 1)
                stack[-1][atom] = stack[-1].get(atom, 0) + cnt
        ref = stack[-1]
        atoms = sorted(list(ref.keys()))
        ans = [atom + (str(ref[atom]) if ref[atom] > 1 else '') for atom in atoms]
        return ''.join(ans)