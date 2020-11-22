"""
https://leetcode.com/problems/unique-morse-code-words/

Transfer word to morse representation, use a set to store the morse representations. 

Time complexity: O(NW), N = len(words), W = wideth of word
"""

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ref = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse = set()
        for word in words:
            tmp = ''
            for c in word:
                idx = ord(c) - ord('a')
                tmp += ref[idx]
            morse.add(tmp)
        return len(morse)