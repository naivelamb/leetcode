"""
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3299/
"""
class Solution:
    def stringShift(self, s: str, shift) -> str:
        total_shift = 0
        for d, i in shift:
            if d == 0:
                total_shift -= i
            else:
                total_shift += i
        actual_shift = abs(total_shift) % len(s)
        if total_shift > 0:
            ans = s[-actual_shift:] + s[:-actual_shift]
        elif total_shift < 0:
            ans = s[actual_shift:] + s[:actual_shift]
        else:
            ans = s
        return ans

sol = Solution()
s = 'abc'
shift = [[0,1], [1,2]]
assert sol.stringShift(s, shift) == 'cab'

s = "abcdefg"
shift = [[1,1],[1,1],[0,2],[1,3]]
assert sol.stringShift(s, shift) == "efgabcd"
