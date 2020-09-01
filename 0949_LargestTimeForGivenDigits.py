"""
https://leetcode.com/problems/largest-time-for-given-digits/
"""
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = h1*10 + h2
            mins = m1*10 + m2
            time = hours*60 + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time
        if ans >= 0:
            hours = ans // 60
            mins = ans % 60
            return f"{hours:02}:{mins:02}"
        else:
            return ""
