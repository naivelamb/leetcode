"""
https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

if n meet the requirements,
n = 3 * a or 3 * a + 1

Time complexity: O(n)
"""
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 3 == 0:
            return self.checkPowersOfThree(n//3)
        elif n % 3 == 1:
            return self.checkPowersOfThree((n - 1)//3)
        else:
            return False