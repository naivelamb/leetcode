"""
https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
Convert and compute
"""
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convrt(word):
            res = 0
            for x in word:
                res = res * 10 + ord(x) - ord('a')
            return res
        
        
        return convrt(firstWord) + convrt(secondWord) == convrt(targetWord)
                