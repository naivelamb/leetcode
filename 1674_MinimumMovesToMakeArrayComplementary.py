"""
https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

For a pair of a, b and a target T,
2 <= T < min(a, b) + 2, we need 2 moves
min(a, b) + 1 <= T < a + b, we need 1 move
T = a + b, we need 0 move
a + b < T <= max(a, b) + limit, we need 1 move
max(a, b) + limit < T <= 2*limit, we need to make 2 moves.

For each pair, we need to record the number of operations. 
delta[i] means how many more changes we need to move when target change from (i-1) to i.

So for a pair for a, b (a <= b)
delta[2] += 2             (baseline value, need 2)
delta[a + 1] -= 1         (need 1 move, so -1 from baseline)
delta[a + b] -= 1         (need 0 move, so -1 further)
delta[a + b + 1] += 1     (need 1 move, so +1)
delta[b + limit + 1] += 1 (need 2 move, so +1 further)

At last we just need to count all possible targets. 

Time complexity: O(n + k)
"""
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        delta, n = collections.Counter(), len(nums)
        for i in range(n//2):
            a, b = nums[i], nums[n - 1 - i]
            a, b = min(a, b), max(a, b)
            delta[2] += 2
            delta[a + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[b + limit + 1] += 1

        curr = 0
        ans = float('inf')
        for i in range(2, 2 * limit + 1):
            curr += delta.get(i, 0)
            ans = min(ans, curr) 
        return ans