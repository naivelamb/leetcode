"""
https://leetcode.com/problems/goat-latin/
"""
class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split(' ')
        ans = []
        for i, w in enumerate(S):
            if w[0] in 'aeiouAEIOU':
                w += 'ma'
            else:
                w = w[1:] + w[0] + 'ma'
            w += 'a' * (i+1)
            ans.append(w)
        return ' '.join(ans)
