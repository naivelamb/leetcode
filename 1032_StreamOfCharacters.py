# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/stream-of-characters/

Store the words in a Trie in their reversed form. 
Query also stored in its reversed form. 
When search the Trie, return True if we see any letter can be used as end of the word. 

Time complexity:
Init: O(l*n), l -> len(words[0]), n -> len(word)
Query: O(k), k -> first letter that can be used as the end of word. 
"""
import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for ch in word:
            curr = curr.children[ch]
        curr.is_word = True
        
        
class StreamChecker:

    def __init__(self, words):
        self.trie = Trie()
        self.q = ''
        for word in words:
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.q = letter + self.q
        curr = self.trie.root
        for ch in self.q:
            curr = curr.children.get(ch)
            if curr is None:
                return False
            if curr.is_word:
                return True
        return curr.is_word