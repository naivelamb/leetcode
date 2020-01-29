"""
https://leetcode.com/problems/k-concatenation-maximum-sum/

When k = 1, we can get it easily in O(len(arr)).
When k == 2, we can simply build new_arr = arr + arr and compute.
When k > 2, we may have the situation:
[------+++|......|......|++------]
The 1st and last parts sum can be computed as [arr + arr]. The middle part is
sum(arr) * (k - 2)

Time complexity: O(2len(arr))
"""
class Solution:
    def kConcatenationMaxSum(self, arr, k):
        def max_sum(arr):
            max_curr, max_so_far = arr[0], arr[0]
            for x in arr[1:]:
                max_curr = max(max_curr+x, x)
                max_so_far = max(max_curr, max_so_far)
            return max_so_far

        if not arr:
            return 0
        s = sum(arr)
        if k == 1:
            return max(0, max_sum(arr)) % (10**9 + 7)
        else:
            return max(0, (k-2)*max(s, 0) + max_sum(arr + arr)) % (10**9 + 7)

sol = Solution()

arr = [1,2]
k = 3
assert sol.kConcatenationMaxSum(arr, k) == 9

arr = [1,-2,1]
k = 5
assert sol.kConcatenationMaxSum(arr, k) == 2

arr = [-1,-2]
k = 7
assert sol.kConcatenationMaxSum(arr, k) == 0
