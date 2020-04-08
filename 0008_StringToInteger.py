"""
https://leetcode.com/problems/string-to-integer-atoi/
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        if not s[0].isdigit() and s[0] not in '-+':
            return 0
        if s.startswith('-'):
            if len(s) <= 1 or not s[1].isdigit():
                return 0
        if s.startswith('+'):
            if len(s) <= 1 or not s[1].isdigit():
                return 0
            s = s[1:]

        isNegative = s.startswith('-')
        if isNegative:
            s = s[1:]
        s_numbers = []
        for i in range(len(s)):
            if s[i].isdigit():
                s_numbers.append(s[i])
            else:
                break
        num = ''.join(s_numbers)
        num = int(num)
        if isNegative:
            num = -num

        if num > 0:
            num = min(num, 2**31 - 1)
        if num < 0:
            num = max(num, -2**31)
        return num
