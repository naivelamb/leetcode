"""
https://leetcode.com/problems/teemo-attacking/
1. Build intervals based on time series and duration.
2. Merge intervals.
3. Calculate total duration time.

Time Complexity: O(N)
"""
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        # build intervals
        intervals = []
        for i, t in enumerate(timeSeries):
            if i == 0:
                intervals.append([t, t + duration])
            else:
                last_int = intervals[-1]
                if t <= last_int[1]:
                    intervals[-1] = [last_int[0], t + duration]
                else:
                    intervals.append([t, t + duration])
                    
        # get answer
        ans = 0
        for t in intervals:
            ans += t[1] - t[0]
        return ans
