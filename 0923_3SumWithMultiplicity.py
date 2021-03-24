"""
https://leetcode.com/problems/3sum-with-multiplicity/

4 situation:
x < y < z
x == y < z
x < y == z
x == y == z

Get count of each number, then just use math combination to find the pairs. 

Time compleixty: O(N + W^2), W = max(arr)
"""
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 101
        for x in arr:
            count[x] += 1
        
        ans = 0
        # x < y < z
        for x in range(101):
            for y in range(x+1, 101):
                z = target - x - y
                if y < z <= 100:
                    ans += count[x] * count[y] * count[z]
        # x == y < z
        for x in range(101):
            z = target - 2*x
            if x < z <= 100:
                ans += count[x] * (count[x] - 1) // 2 * count[z]

        # x < y == z
        for x in range(101):
            if (target - x) % 2 == 0:
                y = (target - x) // 2
                if x < y <= 100:
                    ans += count[x] * count[y] * (count[y] - 1) // 2
        
        # x == y == z
        if target % 3 == 0:
            x = target // 3
            if 0 <= x <= 100:
                ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
        return ans % MOD