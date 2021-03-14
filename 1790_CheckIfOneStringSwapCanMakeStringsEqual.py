"""
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

Find number of unmatched. 
If n == 0, return True
If n == 2, check if they can be same afer swap.
Else return False 
"""
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mis_match = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mis_match.append(i)
        if len(mis_match) == 0:
            return True
        elif len(mis_match) == 2:
            i, j = mis_match
            return (s1[i] == s2[j]) and (s1[j] == s2[i])
        else:
            return False