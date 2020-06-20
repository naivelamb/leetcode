"""
https://leetcode.com/problems/permutation-sequence/

For a sorted permutations of n, first (n-1)! start with 1, next (n-1)! start with 2, etc. In each group of (n-1)! permutations, the first (n-2)! starts with the smallest number.

So we make use of this to build the sequence. We need to locate the position of kth permutation in the group.

1. For the n groups of (n-1)! groups, locate the group of kth permutation: index = k // (n-1)!. Now k before k % (n-1)!

2. For the (n-1) groups of (n-2)! groups, locate the group of kth permutation: index = k // (n-2)!, k = k % (n-2)!.

Time Complexity: O(n^2)
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index = k // math.factorial(n)
            k = k % math.factorial(n)
            permutation += str(numbers[index])
            # remove the handled number
            numbers.remove(numbers[index])
        return permutation
