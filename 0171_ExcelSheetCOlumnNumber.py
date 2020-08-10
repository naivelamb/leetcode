"""
https://leetcode.com/problems/excel-sheet-column-number/

Base-26 integer. Process the string from right to left. Time Complexity: O(N), N = len(s)
"""
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i, ch in enumerate(s[::-1]):
            ans += (ord(ch) - ord('A') + 1)*26**(i)
        return ans
