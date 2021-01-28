"""
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

Greedy. Fill head and tail with 'a' and 'z' as many as possible. 

Let's say we have na 'a', nz 'z', and nm non-'az' characters. 

na + nz + nm = n
na + nz*26 + nm*mid = k

We know nz = (k - n)/25 - nm * (mid - 1)/25
(mid - 1) < 25, nm <= 1, hence nz = (k - n)//25
If (k - n) % 25 == 0, nm = 0 else nm = 1
Then we know na = n - nm - nz

Finally we can assemble the string.

Time complexity: O(n) ==> most of time is at building string.
"""
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ref = '0abcdefghijklmnopqrstuvwxyz'
        n_a = (26 * n - k) // 25
        n_z = (k - n_a) // 26
        mid = k - n_a - n_z * 26
        if mid != 0:
            return n_a * 'a' + ref[mid] + n_z * 'z'
        else:
            return n_a * 'a' + n_z * 'z'
