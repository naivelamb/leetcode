"""
https://leetcode.com/problems/determine-if-string-halves-are-alike/

Split and Count
Time complexity: O(N)
"""
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        n = len(s)
        cnt1, cnt2 = 0, 0
        for i in range(n//2):
            if s[i] in vowels: cnt1 += 1
        for i in range(n//2, n):
            if s[i] in vowels: cnt2 += 1

        return  cnt1 == cnt2