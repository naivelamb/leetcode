"""
https://leetcode.com/problems/happy-number/

For a number 'abcd', check the value of a^2 + b^2 +c^2 + d^2.
Break the loop if we have seen 'abcd', return False
If 'abcd' == '1', return True
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        vals = {n}
        while True:
            ans = 0
            while n:
                tmp = n%10
                ans += tmp**2
                n = n//10
            if ans in vals:
                return False
            else:
                if ans == 1:
                    return True
                else:
                    vals.add(ans)
            n = ans

sol = Solution()
assert sol.isHappy(19) == True
