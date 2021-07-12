"""
https://leetcode.com/problems/find-k-closest-elements/

Use binary search to find the position-i, where for all arr[k] that k < i, arr[k] < x.
Then expand the left and right boundary. 

Time complexity: O(logN + k)
"""
import bisect

class Solution:
    def findClosestElements(self, arr, k, x):
        idx = bisect.bisect_left(arr, x)
        if idx == 0:
            return arr[:k]
        if idx == len(arr):
            return arr[-k:]
        if abs(arr[idx-1] - x) <= abs(arr[idx] - x):
            idx = idx - 1
        res = [arr[idx]]
        a, b = idx - 1, idx + 1

        while len(res) < k:
            if 0 <= a < b < len(arr):
                if abs(arr[a] - x) <= abs(arr[b] - x):
                    res = [arr[a]] + res
                    a -= 1
                else:
                    res.append(arr[b])
                    b += 1
            else:
                if a < 0 and b < len(arr): 
                    res.append(arr[b])
                    b += 1
                if b == len(arr) and a >= 0: 
                    res = [arr[a]] + res
                    a -= 1
        return res
s = Solution()
print(s.findClosestElements([0,0,1,2,3,3,4,7,7,8], 3, 5))
