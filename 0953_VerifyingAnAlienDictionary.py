"""
https://leetcode.com/problems/verifying-an-alien-dictionary/

Build ref dictionary, then do pair-wise comparison. 
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ref = {c: i for i, c in enumerate(order)}

        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            j = 0
            while j < min(len(w1), len(w2)):
                if w1[j] == w2[j]:
                    j += 1
                else:
                    if ref[w1[j]] > ref[w2[j]]:
                        return False
                    else:
                        break
            if j == min(len(w1), len(w2)) and len(w1) > len(w2):
                return False
        return True