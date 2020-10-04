"""
https://leetcode.com/problems/remove-covered-intervals/

Sort the intervals based on (a[0], -a[1]).
So for all the intervals starting with a[0], the first one we saw is the one with maximum intervals. Then we can easily merge those starting with the same number. Furthermore, we only need to check the right boundary to decide wehther merge or not .

Time complexity: O(NlogN)
"""
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda a: (a[0], -a[1]))
        curr_int = intervals[0]
        ans = 1
        for inter in intervals[1:]:
            if inter[1] <= curr_int[1]:
                pass
            else:
                curr_int = inter
                ans += 1
        return ans
