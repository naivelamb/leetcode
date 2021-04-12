"""
https://leetcode.com/problems/sign-of-the-product-of-an-array/

Go through the array, multiply (-1/0/1)
Time complexity: O(N)
"""
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for n in nums:
            if n == 0:
                return 0
            elif n > 0:
                ans *= 1
            else:
                ans *= -1
        return ans