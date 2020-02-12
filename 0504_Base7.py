"""
https://leetcode.com/problems/base-7/
"""
class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return '0'
        x = abs(num)
        ans = ''
        while x:
            ans += str(x%7)
            x // = 7
        if num < 0:
            return '-' + str(ans[::-1])
        return str[ans[::-1]]

sol = Solution()
assert sol.convertToBase7(100) == '202'
assert sol.convertToBase7(-7) == '-10'
