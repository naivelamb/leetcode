# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/remove-invalid-parentheses/

#1 BFS + memory
Given a string, we can compute the minimum remove of left and right to make it 
valid. 
We compute the number, l, r. Each node in the queue are (s, l, r). 
When l == r == 0, we find a valid s, put it into the result. 
We remove '(' when we saw a '(' and we need to remove '(' (l != 0). After 
removing, we put the new string back to queue under following conditions:
	1. The removing makes the string closer to the target. 
The sting has never been seen before. 
"""
import collections
class Solution:
    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':
        l, r = self.need_remove(s)
        if self.isValid(l, r):
            return [s]
        res, seen = [], set()
        queue = collections.deque([(s, l, r)])
        seen.add(s)
        while queue:
            s, l, r = queue.popleft()
            if self.isValid(l, r):
                res.append(s)
                continue
            for i in range(len(s)):
                if s[i] == '(' and l > 0:
                    new_s = s[:i] + s[i+1:]
                    new_l, new_r = self.need_remove(new_s)
                    if new_l == l - 1 and new_s not in seen:
                        seen.add(new_s)
                        queue.append((new_s, new_l, new_r))
                if s[i] == ')' and r > 0:
                    new_s = s[:i] + s[i+1:]
                    new_l, new_r = self.need_remove(new_s)
                    if new_r == r - 1 and new_s not in seen:
                        seen.add(new_s)
                        queue.append((new_s, new_l, new_r))
        return res
        
    def need_remove(self, s):
        # compute the '(' and ')' that need to be removed
        l, r = 0, 0
        for ch in s:
            if ch == '(':
                l += 1
            if ch == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
        return l, r
    
    def isValid(self, l, r):
        return l == 0 and r == 0
    
s = Solution()
a = '()())()'
print(s.removeInvalidParentheses(a))
a = ')('
print(s.removeInvalidParentheses(a))