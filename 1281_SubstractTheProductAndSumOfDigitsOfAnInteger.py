"""
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

Get the digit one by one.
Time complexity: O(N), where N is the number of digits of n.
"""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, summ = 1, 0
        while n:
            prod *= (n%10)
            summ += (n%10)
            n //= 10
        return prod - summ

sol = Solution()
assert sol.subtractProductAndSum(234) == 15
assert sol.subtractProductAndSum(4421) == 21
