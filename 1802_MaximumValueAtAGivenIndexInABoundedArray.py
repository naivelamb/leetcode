"""
https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

If we know nums[index], the minimum sum would be use it as peak, then go descending by 1 to front and back. 

Binary search for all possible maxSum.

Time complexity: O(log(maxSum))
"""
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def fn(n, x):
            # compute minimum sum give peak value x and number of position n
            if x > n:
                return (x + x - n + 1) * n // 2
            else:
                return x*(1+x)//2 + n - x

            lo, hi = 0, maxSum
            while lo < hi:
                mid = (lo + hi)//2
                total = fn(index, mid - 1) + fn(n - index, mid)
                if total <= maxSum:
                    lo = mid
                else:
                    hi = mid - 1
            return lo