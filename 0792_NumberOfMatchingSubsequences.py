"""
https://leetcode.com/problems/number-of-matching-subsequences/

we store all words based  on the first letter, then go through the string. 

Take all words corresponding the the first letter, remove the first, and then put it back to the first-letter based database. 

If the word is of length 1, then it is the subsequence. 

Time complexity: O(N + ML)
N = len(s)
M = len(words)
L = len(words[i])
"""
class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        heads = [[] for _ in range(26)]
        for word in words:
            heads[ord(word[0]) - ord('a')].append(word)
        
        res = 0
        for c in s:
            i = ord(c) - ord('a')
            old_words = heads[i]
            heads[i] = []
            while old_words:
                w = old_words.pop()
                if len(w) == 1:
                    res += 1
                else:
                    heads[ord(w[1]) - ord('a')].append(w[1:])
        return res        

s = 'abcde'
words = ['a', 'bb', 'acd', 'ace']
S = Solution()
assert S.numMatchingSubseq(s, words) == 3