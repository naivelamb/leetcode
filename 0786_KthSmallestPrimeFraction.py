"""
https://leetcode.com/problems/k-th-smallest-prime-fraction/

N = len(A)

1) Brute force
Generate all the pairs (O(N^2)), heapify it (O(N^2)), then pop K (Klog(N^2)).
Time complexity: O(max(N^2, KlogN^2))

2) Binary Search.
Let under(x) find the number of fractions under x and return the largest x.
This part is O(N).
Then we can use binary search to find x, such that there are K fractions smaller than x.

Time Complexity: NlogW, where W is the window of binary search width. We used 1e-9, so W = 10^9. 
"""
class Solution:
    def kthSmallestPrimeFraction(self, A, K: int):
        from fractions import Fraction
        def under(x):
            # return the number of fractions < x,
            # and the largest fraction
            count = best = 0
            i = -1
            for j in range(1, len(A)):
                while A[i+1] < A[j] * x:
                    i += 1
                count += i + 1
                if i >= 0:
                    best = max(best, Fraction(A[i], A[j]))
            return count, best

        lo, hi = 0, 1
        while hi - lo > 1e-9:
            mid = (lo + hi) / 2
            count, best = under(mid)
            if count < K:
                lo = mid
            else:
                ans = best
                hi = mid
        return ans.numerator, ans.denominator

sol = Solution()
assert sol.kthSmallestPrimeFraction([1,2,3,5], 3) == [2,5]
assert sol.kthSmallestPrimeFraction([1,7], 1) == [1,7]
