# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/camelcase-matching/

Compare each word with pattern, two pointer.

Time complexity: O(nm), n -> len(queries), w -> len(word)
"""
class Solution:
    def camelMatch(self, queries, pattern):
        def helper(word, pattern):
            # if word can be represented by the pattern
            i, j = 0, 0
            while i < len(word) and j < len(pattern):
                if word[i] == pattern[j]:
                    i += 1
                    j += 1
                else:
                    if word[i].islower():
                        i += 1
                    else:
                        return False
            if j != len(pattern):
                return False
            else:
                while i < len(word):
                    if not word[i].islower():
                        return False
                    i += 1
                return True
        return [helper(w, pattern) for w in queries]
