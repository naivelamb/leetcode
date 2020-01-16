"""
https://leetcode.com/problems/score-after-flipping-matrix/

i-th col from the right contribute 2^i to the score.

2^n > 2^(n-1) + 2^(n-2) + ... + 2^0

So if the first col in the row is 0, the row must be flipped.
Then we check each col. Only flip the col if and only if there are more '0's than '1's.

Time complexity: O(mn), m=len(A), n=len(A[0])
"""

class Solution:
    def matrixScore(self, A) -> int:
        m, n = len(A), len(A[0])
        ans = 0

        # flip row
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] = 1 - A[i][j]
            else:
                continue

        # flip col
        for j in range(n):
            cnt = sum(A[i][j] for i in range(m))
            ans += max(cnt, m - cnt) * (2**(n-j-1))

        return ans


test = [
        [0,0,1,1],
        [1,0,1,0],
        [1,1,0,0],
        ]
ans = 39

sol = Solution()
#print(sol.matrixScore(test))
assert ans == sol.matrixScore(test)
