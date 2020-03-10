"""
https://leetcode.com/problems/maximum-69-number/
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = list(str(num))
        for i, char in enumerate(ans):
            if char == '6':
                ans[i] = '9'
                break
        ans = ''.join(ans)
        return int(ans)

sol = Solution()
assert sol.maximum69Number(9669) == 9969
assert sol.maximum69Number(9996) == 9999
assert sol.maximum69Number(9999) == 9999
