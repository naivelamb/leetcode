"""
https://leetcode.com/problems/detect-capital/
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            n_upper = 0
            for c in word[1:]:
                if c.isupper():
                    n_upper += 1
            if n_upper == 0 or n_upper == len(word) - 1:
                return True
            else:
                return False
        else:
            for c in word[1:]:
                if c.isupper():
                    return False
        return True        
