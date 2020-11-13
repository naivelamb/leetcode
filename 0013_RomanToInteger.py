"""
https://leetcode.com/problems/roman-to-integer/

Compare current value with previous value. 
If curr == prev: add to temp accumulation.
If curr > prev: add (curr - tmp_accu) to total and set curr = 0
If curr < prev: add tmp_accu to total and set tmp_accu = curr

Time complexity: O(N)
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        ref = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans, i, tmp = 0, 1, ref[s[0]]
        while i < len(s):
            if ref[s[i]] == ref[s[i-1]]:
                tmp += ref[s[i]]
            elif ref[s[i]] > ref[s[i-1]]:
                ans += ref[s[i]] - tmp
                tmp = 0
            else:
                ans += tmp
                tmp = ref[s[i]]
            i += 1
        ans += tmp
        return ans