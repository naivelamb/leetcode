"""
https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

Deci-binary only contains 0 or 1, if the max digit of n is x, then we need at least x numbers to sum up to digit x. 

Take 135 as an example, we initialize with 5 3-digit deci-binary numbers 
000
000
000
000
000

We need 1 "1"s at the 1st digit, 3 "1"s at the 2nd digit and 5 "1"s at the 3rd digt, which results in,
111
011
011
001
001

Finally we have 111 + 11 + 11 + 1 + 1 = 135

Time complexity O(L), L = len(n)
"""
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))