"""
https://leetcode.com/problems/first-bad-version/

Binary search.
Time compexity: O(logN)
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                if mid == 1: #first version bad, return
                    return mid
                else:
                    if not isBadVersion(mid - 1): #previous good, return
                        return mid
                    else: # bad version previous
                        r = mid - 1
            else:
                l = mid + 1
        return l
