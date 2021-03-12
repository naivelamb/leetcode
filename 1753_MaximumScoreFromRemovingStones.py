"""
https://leetcode.com/problems/maximum-score-from-removing-stones/

Always remove from the least and the most pile. If the least pile is 0, take from the 2nd and 3rd pile.


"""
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        cnt = [a, b, c]
        cnt.sort()
        ans = 0
        while cnt[1] != 0 and cnt[0] != 0:
            cnt[0] -= 1
            cnt[1] -= 1
            ans += 1
            cnt.sort()
        ans += cnt[1]
        return ans