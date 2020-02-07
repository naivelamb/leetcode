"""
https://leetcode.com/problems/count-of-range-sum/

1) Brute force.
Compute pre_sum[i] = sum(nums[:i])
For each i, count number of j such that:
0 <= j < i, lower <= pre_sum[j] - pre_sum[i] <= upper

Time complexity: O(N^2)

2) Prefix sum + hashmap
Store the prefix sum into a dictionary.

Time complexity: O(N + (upper - lower + 1) * N)

3) First build prefix sum. For each i, if the prefix_sum[:i] is sorted, we can easily find the number of range sum using bianry search.
Time complexity: O(NlogN)
"""
class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        count, s = 0, 0
        sorted_sums = [0]
        for x in nums:
            s += x
            l = bisect.bisect_left(sorted_sums, s - upper)
            r = bisect.bisect_right(sorted_sums, s - lower)
            count += r - l
            bisect.insort(sorted_sums, s)
        return count


sol = Solution()

nums = [-2, 5, -1]
lower = -2
upper = 2
assert sol.countRangeSum(nums, lower, upper) == 3
