# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

DP[i, j] => length of longest fib seq ending with i and j.
DP[j, k] = DP[i, j] + 1 if A[i] + A[j] = A[k]

Time Complexity: O(n^2)
"""

class Solution:
    def lenLongestFibSubseq(self, A: 'List[int]') -> 'int':
        dp = {}
        ref = {x: i for i, x in enumerate(A)}
        ans = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                target = A[i] + A[j]
                k = ref.get(target, -1)
                if k > j:
                    dp[j, k] = dp.get((i, j), 2) + 1
                    ans = max(ans, dp[j, k])
        return ans if ans > 2 else 0

s = Solution()
a = [1,2,3,4,5,6,7,8]
print(s.lenLongestFibSubseq(a))
a = [1,3,7,11,12,14,18]
print(s.lenLongestFibSubseq(a))