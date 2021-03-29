"""
https://leetcode.com/problems/maximize-number-of-nice-divisors/

Let's assume the number is,
p1^a1 + p2^a2 + ... p_i^a_i + ... + p_n^a_n 
where p_i is prime and p_i != p_j for any i != j.

So we have 
a1 + a2 + ... + a_i + ... + a_n = N
and we want to maximize 
a1*a2*a3*...*a_i*...a_n.

We know 
a1 + a2 + ... + a_i + ... + a_n >= n(a1*a2*a3*...*a_i*...a_n)^(1/n)

The best split is when we make number equal to 2 or 3. 
If we have 4 -> 2*2
If we have 5 -> 2*3
If we have 6 -> 3*3

Use pow to find the value, pass MOD to it to reduce complexity. 

Time compleixty: O(logn)
"""
class Solution:
    def maxNiceDivisors(self, n: int) -> int:
        M = 10**9 + 7
        if n <= 3: return n
        if n % 3 == 0: return pow(3, n//3, M)
        if n % 3 == 1: return pow(3, (n-4)//3, M) * 4 % M
        return (2 * pow(3, n//3, M)) % M