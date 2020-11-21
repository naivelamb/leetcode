"""
https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

N = str(n), k = len(N)
If we form a number less than k digit, it automatically meets the requirements. 
Hence we have sum(len(digits) ** i for i in range(1, k))

For exactly k digit, we can fix first-i digit by letting digit from [0, i-1] exactly the same to n, i-th digit smaller than N[i], in this way we have
sum(c < N[i] for c in digits) * (len(digits) ** (n - i - 1))

When we see a N[i] that doesn't exist in digits, we need to break. 

At the end we need to check whether we can make a number exactly the same as n.

Time complexity: O(logn) (since len(str(n)) = logn)
"""
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        N = str(n)
        n = len(N)
        res = sum(len(digits) ** i for i in range(1, n))
        i = 0
        while i < n:
            res += sum(c < N[i] for c in digits) * (len(digits) ** (n - i - 1))
            if N[i] not in digits:
                break
            i += 1
        return res + (i == n)