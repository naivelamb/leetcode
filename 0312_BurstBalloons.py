# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/burst-balloons/

#1 BFS with cache
Try to burst all possible balloons at each step, remember the coins got so far. 
In the cache, key -> remain balloons; val -> coins got so far.
Time Complexity: O(N!) => TLE

#2 Divide and conquer, top-down
Expand nums to [1] + nums + [1]
coins[i][j] => max coins can be get by using i as left and j as right
Final answer is coins[0][n-1]
coins[i][j] = max(coins[i][j], coins[i][k] + coins[k][j] + nums[i]*nums[k]*nums[j])
for all k, i < k < j
coins[i][j] can be got recursively.

#3 DP
Same idea as #2, but bottom-up. When j - i == 2, the answer is certain. We build
the coins array from it, then keep going up until we get coins[0][n-1] 
"""
import collections
class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        coins = [[0] * n for _ in range(n)]
        
        def helper(i, j):
            if coins[i][j] or j == i + 1:
                return coins[i][j]
            ans = 0
            for k in range(i + 1, j):
                ans = max(ans, nums[i]*nums[k]*nums[j] + helper(i, k) + helper(k, j))
            coins[i][j] = ans
            return ans
        return helper(0, n-1)
    
    def maxCoins_bottomUp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        coins = [[0] * n for _ in range(n)]
        
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i+1, j):
                    coins[i][j] = max(coins[i][j], 
                         nums[i]*nums[k]*nums[j] + coins[i][k] + coins[k][j])
        return coins[0][n-1]
    
    def maxCoins_bfs(self, nums):
        """
        Time Complexity: O(N!) => TLE
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        queue = collections.deque()
        queue.append([nums, 0])
        ans = 0
        while queue:
            nums, coins = queue.popleft()
            key = tuple(nums) # O(N)
            if cache.get(key, 0) > coins:
                continue
            else:
                cache[key] = coins
            n = len(nums)    
            for i in range(n):
                new_nums = nums[:i] + nums[i+1:]
                n_left = 1 if i - 1 == -1 else nums[i - 1]
                n_right = 1 if i + 1 == n else nums[i + 1]
                new_coins = coins + n_left * n_right * nums[i]
                if not new_nums:
                    ans = max(ans, new_coins)
                else:
                    new_key = tuple(new_nums)
                    if new_coins > cache.get(new_key, 0):
                        cache[new_key] = new_coins
                        queue.append([new_nums, new_coins])
        return ans

nums = [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]
s = Solution()
print(s.maxCoins_bfs(nums))