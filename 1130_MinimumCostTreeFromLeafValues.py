"""
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

1) Brute force DP
dp[i, j] is the answer for subarray arr[i, j].
dp[i, j] = dp[i, k] + dp[k+1, j] + max(arr[i, k]) * max(arr[k+1, j])
For each i, j, we need to go through all k in (i, j).

Time complexity: O(N^3), Space complexity: O(N^2)

2) Stack
Everytime we choose two neighbors a and b, we remove the smaller one with cost a*b.
What is the minimum cost to remove the whole array?
If b >= a, we will remove a. To minimize the cost, we need to minimize b.
b has two candidates: the first bigger number on the left; the first bigger number in the right.
The cost to remove a is a*min(left, right).
Therefore, we need to find next greater element on the left and right.

Time complexity: O(N)
"""
class Solution:
    def mctFromLeafValues(self, arr):
        res = 0
        stack = [float('inf')]
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res

    def mctFromLeafValues_dp(self, arr):
        self.memo = {}
        def dp(i, j):
            if j <= i:
                return 0
            if (i,j) not in self.memo:
                res = float('inf')
                for k in range(i+1, j+1):
                    res = min(dp(i, k-1) + dp(k, j) + max(arr[i:k]) * max(arr[k:j+1]), res)
                self.memo[(i,j)] = res
            return self.memo[(i, j)]
        return dp(0, len(arr) - 1)

sol = Solution()

arr = [6, 2, 4]
assert sol.mctFromLeafValues(arr) == 32
