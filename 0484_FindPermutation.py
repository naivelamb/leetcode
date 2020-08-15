"""
https://leetcode.com/problems/find-permutation/

We need to return the smallest lexicographically permutation, this means the array should mutate from the min array: [1, 2, 3, 4, 5, ..., n].

For the pattern 'DDIIIID', we need to reverse the first 3 digit,
[3,2,1,4,5,6,7,8]
And then change the last 2 digits to:
[3,2,1,4,5,6,8,7]

So we need to put number in to a stack, and pop all the existing number in stack to answer when we see 'I', and then move to the next digit.

Time complexity: O(N)
"""
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        res, stack = [], []
        for i in range(len(s)):
            stack.append(i+1)
            if s[i] == 'I':
                while stack:
                    res.append(stack.pop())
        stack.append(len(s) + 1)
        while stack:
            res.append(stack.pop())
        return res
