"""
https://leetcode.com/problems/remove-palindromic-subsequences/

The results are either 0, 1 or 2. 

If s is empty, 0.
If s is palindromic, 1.
Else, 2 (remove all 'a' then all 'b').

"""
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        elif s == s[::-1]:
            return 1
        else:
            return 2