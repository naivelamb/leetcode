# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/group-anagrams/

anagrams: all characters are the same, but different order.
hashmap, key -> tuples store cnt for all 26 chars
"""
import collections
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ref = collections.defaultdict(list)
        for word in strs:
            mask = [0] * 26
            for c in word:
                mask[ord(c) - ord('a')] += 1
            key = tuple(mask)
            ref[key].append(word)
        return [ref[key] for key in ref]