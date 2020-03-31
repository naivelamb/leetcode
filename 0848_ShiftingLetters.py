"""
https://leetcode.com/problems/shifting-letters/

First compute prefix sum, then go over the string to compute the shifted results.
Time complexity: O(N)
"""
class Solution:
    def shiftingLetters(self, S: str, shifts) -> str:
        ans = list(S)
        real_shifts = [0]
        for x in shifts[::-1]:
            real_shifts.append(real_shifts[-1] + x)
        real_shifts = real_shifts[::-1][:-1]
        for i, x in enumerate(real_shifts):
            idx = ord(ans[i]) + x
            if idx - ord('a') > 26:
                idx = ord('a') + (idx - ord('a')) % 26
            ans[i] = chr(idx)
        return ''.join(ans)

sol = Solution()
assert sol.shiftingLetters("abc", [3,5,9]) == "rpl"
