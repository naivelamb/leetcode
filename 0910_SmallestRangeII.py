"""
https://leetcode.com/problems/smallest-range-ii/

After getting B, if we add another K to it, the results won't change. So it is same as adding 0 or 2K to it. 

Sort first. Then we have ans res = A[-1] - A[0]. 
Now for each A[i], we try to add 2K to see if we can make the difference smaller. 

Time complexity: O(nlogn)

"""
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            mn = min(A[i+1], A[0] + 2 * K)
            mx = max(A[-1], A[i] + 2 * K)
            res = min(res, mx - mn)
        return res