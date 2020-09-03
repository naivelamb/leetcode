"""
https://leetcode.com/problems/repeated-substring-pattern/

Check all the possible substring patterns.
Time Complexity: O(N^2)
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2+1):
            if n % i == 0:
                k = n // i
                if s == s[:i]*k:
                    return True
        return False
