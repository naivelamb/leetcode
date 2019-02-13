# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/word-pattern/

Hashmap store relation between pattern and strings.
"""
class Solution:
    def wordPattern(self, pattern: 'str', str: 'str') -> 'bool':
        words = str.split()
        if len(words) != len(pattern):
            return False
        ref = {}
        for i, p in enumerate(pattern):
            if p in ref:
                if ref[p] != words[i]:
                    return False
            else:
                ref[p] = words[i]
        return len(set(ref.keys())) == len(set(ref.values()))

s = Solution()
pattern = "abba"
str = "dog cat cat dog"
print(s.wordPattern(pattern, str))
pattern = "abba"
str = "dog cat cat fish"
print(s.wordPattern(pattern, str))
pattern = "abba"
str = "dog dog dog dog"
print(s.wordPattern(pattern, str))