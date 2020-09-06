"""
https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

Get the frequency.
For a pair of (n1, n2), if the 3rd number exisits, then
n1**2 % n2 == 0
n3 = n1**2 // n2
We can check whether n3 exists or not. If exisits, the # of triplets is,
cnt1[n1] * cnt2[n2] * cnt2[n3]
Be careful if n2 == n3, for this case, the # of triplets should be,
cnt1[n1] * cnt2[n2] * (cnt2[n2] - 1) / 2

We can make sure n1 < n2 to avoid duplication.

Time Complexity: O(mn)
"""
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        def helper(cnt1, cnt2):
            ans = 0
            visited = set()
            for x in cnt1:
                for y in cnt2:
                    if x**2 % y == 0:
                        y1 = x**2 // y
                        if (y, y1) in visited:
                            continue
                        else:
                            visited.add((y, y1))
                            visited.add((y1, y))
                        if y1 not in cnt2:
                            continue
                        if y == y1:
                            ans += cnt1[x]*math.comb(cnt2[y], 2)
                        else:
                            ans += cnt1[x]*cnt2[y]*cnt2[y1]
            return ans

        return helper(cnt1, cnt2) + helper(cnt2, cnt1)
