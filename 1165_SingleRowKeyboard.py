"""
https://leetcode.com/problems/single-row-keyboard/
"""
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ref = {}
        for i, ch in enumerate(keyboard):
            ref[ch] = i
        curr_pos, ans = 0, 0
        for ch in word:
            ans += abs(ref[ch] - curr_pos)
            curr_pos = ref[ch]
        return ans

sol = Solution()
assert sol.calculateTime('abcdefghijklmnopqrstuvwxyz', 'cba') == 4
assert sol.calculateTime('pqrstuvwxyzabcdefghijklmno', 'leetcode') == 73
