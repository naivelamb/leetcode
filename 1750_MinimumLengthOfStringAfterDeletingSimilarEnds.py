"""
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

Two pointers. Try to remove as many characters as possible in one pass.

Time complexity: O(N)
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                while s[l + 1] == s[l] and l + 1 < r:
                    l += 1
                while s[r - 1] == s[r] and r - 1 > l:
                    r -= 1
            else:
                break
            l += 1
            r -= 1
        if r < l:
            return 0
        return r - l + 1