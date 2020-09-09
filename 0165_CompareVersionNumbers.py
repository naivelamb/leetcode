"""
https://leetcode.com/problems/compare-version-numbers/
Convert to list, pad short one with trailing 0. Check element one by one
Time Complexity: O(n), n = max(len(version1), len(version2))
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        n = max(len(v1), len(v2))
        v1 += [0]*(n - len(v1))
        v2 += [0]*(n - len(v2))
        for n1, n2 in zip(v1, v2):
            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1
        return 0
