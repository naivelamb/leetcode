"""
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/
"""
class Solution:
    def countElements(self, arr: List[int]) -> int:
        cnt = {}
        for n in arr:
            cnt[n] = cnt.get(n, 0) + 1
        ans = 0
        for n in cnt:
            if n + 1 in cnt:
                ans += cnt[n]
        return ans

sol = Solution()
assert sol.countElements([1,2,3]) == 2
assert sol.countElements([1,1,3,3,5,5,7,7]) == 0
assert sol.countElements([1,3,2,3,5,0]) == 3
assert sol.countElements([1,1,2,2]) == 2
