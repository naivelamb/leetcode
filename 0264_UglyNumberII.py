"""
https://leetcode.com/problems/ugly-number-ii/
U_k is the kth ugly number, it will genearte 3 new ugly numbers:
U_k*2, U_k*3, U_k*5

These three ugly number will generate 9 ugly number, in 3 sorted list, and we need to merge them. (merge k-sorted list)

Everytime we add one number to the big sorted array, essential we are tracking the number that needs to be multiplied by 2, 3, 5 respectively.

DP + pointer, time complexity: O(N)
"""
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return None
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[1] = 1
        pointer2, pointer3, pointer5 = 1, 1, 1
        for i in range(2, n+1):
            dp[i] = min(2*dp[pointer2], 3*dp[pointer3], 5*dp[pointer5])
            if dp[i] == 2*dp[pointer2]:
                pointer2 += 1
            if dp[i] == 3*dp[pointer3]:
                pointer3 += 1
            if dp[i] == 5*dp[pointer5]:
                pointer5 += 1
        return dp[n]             
