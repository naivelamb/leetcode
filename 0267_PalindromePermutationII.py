# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/palindrome-permutation-ii/

First make sure the string can form palindrome. 
If so, the problem is generate permutation with duplicate elements. 
"""
class Solution:
    def generatePalindromes(self, s: 'str') -> 'List[str]':
        ref = {}
        for c in s:
            ref[c] = ref.get(c, 0) + 1
        odd, odd_char, half_string = 0, '', ''
        for c in ref:
            if ref[c] % 2:
                odd += 1
                odd_char = c
                if odd > 1:
                    return []
            half_string += c * (ref[c] // 2)
        if len(s) <= 1 or len(ref) <= 1:
            return [s]
        
        used = [False] * len(half_string)
        self.ans = []
        self.dfs(half_string, '', used)
        return [x + odd_char + x[::-1] for x in self.ans]
        
    def dfs(self, half_string, curr, used):
        if len(curr) == len(half_string):
            self.ans.append(curr)
            return
        
        for i in range(len(half_string)):
            if used[i]:
                continue
            if i >= 1 and half_string[i] == half_string[i-1] and used[i-1]:
                continue
            curr += half_string[i]
            used[i] = True
            self.dfs(half_string, curr, used)
            curr = curr[:-1]
            used[i] = False

a = 'aabb'
b = 'aacbb'
s = Solution()
print(s.generatePalindromes(a))
print(s.generatePalindromes(b))