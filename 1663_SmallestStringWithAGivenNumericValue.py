"""
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

Greedy. Fill head and tail with 'a' and 'z' as many as possible. 

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
