"""
https://leetcode.com/problems/valid-parenthesis-string/
We count open parenthesis.
cmax -> maximum open parethesis. # of '(' that COULD be paired, all * count as '('.
cmin -> minimum open parethesis. # of '(' that MUST be paired.

Time complexity: O(N), N = len(s)
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin, cmax = 0, 0
        for ch in s:
            if ch == '(':
                cmin += 1
                cmax += 1
            elif ch == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            elif ch == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0

sol = Solution()
assert sol.checkValidString("()") == True
assert sol.checkValidString("(*)") == True
assert sol.checkValidString("(*))") == True
