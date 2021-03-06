"""
https://leetcode.com/problems/short-encoding-of-words/
#Order does not matter! 

A word w1 can be saved from putting in the encoding if we can find another word w2, such that,
w1 = w2[i:],
Obviously, longer string has bigger chance being stored.

Store all words in a set, then check each tail part of every word. 

Time complexity: O(NK^2)
N = len(words)
K = len(word)
"""
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return sum(len(w) + 1 for w in s)