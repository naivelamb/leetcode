"""
https://leetcode.com/problems/mirror-reflection/

Assume there are k reflections after reaching one receptor, then (k * q) % p == 0

Hence k = p // gcd(p, q)

if k is even, must be 2.
If k is odd, either 0 or 1.
We need to check whether t = (k * q // p) = (q // gcd(p, q)) is even or odd.
If t is even, we are at 0; else, we are at 1.

Time complexity: O(logP)
"""
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = math.gcd(p, q)
        k = p // g
        if k % 2 == 0:
            return 2
        else:
            if (q // g) % 2 == 0:
                return 0
            else:
                return 1