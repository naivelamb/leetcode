"""
https://leetcode.com/problems/count-number-of-homogenous-substrings/

For a homogenous substring of length k, the number of possible homogenou strings are,
(1 + k) * k / 2

So we just need to find the number of homogenous substring. Two pointer.

Time complexity: O(N)

"""
class Solution:
    def countHomogenous(self, s: str) -> int:
        ans, i = 0, 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            ans += (j - i + 1) * (j - i) // 2
            i = j
        return ans % (10**9 + 7)