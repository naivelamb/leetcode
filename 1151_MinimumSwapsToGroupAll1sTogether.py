"""
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

The number of ones that needs to be grouped together are number of ones in the array.
Let's say we have k 1s in the array.
Then we just need to find the minimum number of 0s in the subarray of length k.

So we just need to maintain a sliding window of size k.
Time complexity: O(N), N is the length of the array.
"""
class Solution:
    def minSwaps(self, data) -> int:
        # count ones
        k = 0
        for x in data:
            if x == 1:
                k += 1

        # sliding window
        cnt, ans = 0, k
        for i in range(len(data)):
            if i < k:
                if data[i] == 0:
                    cnt += 1
                if i == k - 1:
                    ans = min(cnt, ans)
            else:
                if data[i] == 0:
                    cnt += 1
                if data[i-k] == 0:
                    cnt -= 1
                ans = min(cnt, ans)
        return ans

sol = Solution()
data = [1,0,1,0,1]
assert sol.minSwaps(data) == 1
data = [0,0,0,1,0]
assert sol.minSwaps(data) == 0
data = [1,0,1,0,1,0,0,1,1,0,1]
assert sol.minSwaps(data) == 3
