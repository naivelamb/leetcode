"""
https://leetcode.com/problems/set-mismatch/
1). Create a set for numbers from 1 to n. Go through nums, remove the num if it exists in the set, else store it (duplicate). The last remain element in the set is the missing one.
Time complexity: O(N)

2). Math. 
Let's say the missing value is A, duplicate value is B. 
So sum(nums) - sum(list(range(1, n + 1))) = A - B = X
sum(nums**2)  - sum(i**2 for i in range(1, n + 1)) = A**2 - B**2 = Y
So, 
Y/X = A + B
A = (Y/X + X) / 2
B = (Y/X - X) / 2
"""
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        vals = set(list(range(1, n + 1)))
        ans = []
        for x in nums:
            if x in vals:
                vals.remove(x)
            else:
                ans.append(x)
        for v in vals:
            ans.append(v)
        return ans

    def findErrorNums_math(self, nums: List[int]) -> List[int]:
        n = len(nums)
        X = sum(nums) - sum(x for x in range(1, n + 1))
        Y = sum(x**2 for x in nums) - sum(x**2 for x in range(1, n + 1))

        return [int((Y/X + X)//2), int((Y/X - X)//2)]