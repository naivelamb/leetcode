"""
https://leetcode.com/problems/divide-two-integers/

For the i-th iteration, try to deduct
2**(i - 1) * divisor
from dividend, and add 2**(i-1) to ans. 
If dividend < 2**(i - 1) * divisor, need to reset divisor to raw divisor. 
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        positive = (dividend < 0) == (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)

        ans = 0
        k, mult = divisor, 1
        while dividend >= divisor:
            dividend -= k
            k += k
            ans += mult
            mult += mult
            if dividend < k:
                k = divisor
                mult = 1
        
        if positive:
            return min(ans, 2**31 - 1)
        else:
            return max(-ans, -2**31)