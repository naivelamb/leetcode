"""
https://leetcode.com/problems/reach-a-number/

We first find the smallest n, such that
(1 + n) * n / 2 <= abs(target)

Then we find the first n, such that
(1 + n) * n / 2 >= abs(target)
&
((1 + n) * n / 2 - abs(target)) % 2 == 0

This is because when we flip a sign for k, we are getting 
(1 + n) * n / 2 - 2 * k
suggesting that the differece should be an even number.

"""
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = int(((1 + 4*target)**0.5 - 1)/2)
        while True:
            v = (1 + n) * n / 2 - target
            if v >= 0:
                if v % 2 == 0:
                    return n
            n += 1