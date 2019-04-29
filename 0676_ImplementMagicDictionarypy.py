# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/implement-magic-dictionary/

Store words in a hashmap based on length.
When search, compare the word with all candidates of the same length, see if the 
difference is exactly one. 

Time complexity: 
    build -> O(n); 
    search -> O(mk), m -> number of words of same length, k -> word length
"""
import collections
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ref = collections.defaultdict(list)

    def buildDict(self, dict) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.ref[len(word)].append(word)

    def search(self, word) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word 
        after modifying exactly one character
        """
        for ref_word in self.ref[len(word)]:
            cnt = 0
            for i in range(len(word)):
                if word[i] != ref_word[i]:
                    cnt += 1
            if cnt == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
