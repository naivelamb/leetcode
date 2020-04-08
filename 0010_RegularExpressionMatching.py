"""
https://leetcode.com/problems/regular-expression-matching/
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return False

sol = Solution.isMatch()
assert sol.isMatch("aa", "a") == False
assert sol.isMatch("aa", "a*") == True
assert sol.isMatch("aa", ".*") == True
assert sol.isMatch("aab", "c*a*b") == True
assert sol.isMatch("mississippi", "mis*is*p*.") == False
