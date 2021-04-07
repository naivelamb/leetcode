"""
https://leetcode.com/problems/minimum-operations-to-make-array-equal/

Math, meet at middle. 

target = sum(arr)/n = (1 + 2 * n - 1) * n / 2 / n = n

k = n // 2
if n % 2 == 0: (1 + 2 * k - 1) * k / 2 = k**2
else: (2 + 2 * k) * k / 2 = k * (k + 1)

time complexity: O(1)
"""
class Solution:
    def minOperations(self, n: int) -> int:
        k = n // 2
        if n % 2 == 0: return k**2
        else: return k * (k + 1)