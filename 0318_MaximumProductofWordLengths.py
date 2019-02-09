# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/maximum-product-of-word-lengths/

Brute force: O(n^2*w), w -> length of word

Since we only have 26 lower letters, we can use a 26-digit binary mask to record
each word. To check whether two words have common letter or not, we can use 
bit operator '&', which is O(1). Therefore, the overall complexity is reduced to 
O(n^2)

A slightly better approach, use hashmap to record the longest word length for 
each mask, the code will be more efficient when there are shared masks.
"""
class Solution:
    def maxProduct(self, words: 'List[str]') -> 'int':
        masks = []
        for w in words:
            mask = [0] * 26
            for c in w:
                mask[ord(c) - ord('a')] = 1
            key = int(''.join(map(str, mask)), 2)
            masks.append(key)
        
        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                m1, m2 = masks[i], masks[j]
                if m1 & m2 == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
        
        
    def maxProduct_dict(self, words: 'List[str]') -> 'int':
        ref = {}
        for w in words:
            mask = [0]*26
            for c in w:
                mask[ord(c) - ord('a')] = 1
            key = int(''.join(map(str, mask)), 2)
            ref[key] = max(ref.get(key, 0), len(w))
        
        ans = 0
        for k1 in ref:
            for k2 in ref:
                if k1 != k2:
                    if k1 & k2 == 0:
                        ans = max(ans, ref[k1]*ref[k2])
        return ans
