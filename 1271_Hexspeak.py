"""
https://leetcode.com/problems/hexspeak/
"""
class Solution:
    def toHexspeak(self, num: str) -> str:
        num = int(num)
        res = ''
        while num > 0:
            num, cur = divmod(num, 16)
            if 2 <= cur <= 9: return 'ERROR'
            if cur == 0:
                res += 'O'
            elif cur == 1:
                res += 'I'
            else:
                res += chr(cur - 10 + ord('A'))
        return res[::-1]

sol = Solution()
assert sol.toHexspeak('257') == 'IOI'
assert sol.toHexspeak('3') == 'ERROR'
