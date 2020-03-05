"""
https://leetcode.com/problems/maximum-profit-in-job-scheduling/
dp[t] = p means that for time [1, time], the most profit is p.

For a new [start, end, profit], we need to find the right location of it in dp, then check dp[i] + profit > dp[i-1] to decide whether we add it to dp. If we add to it, we extend dp to dp[end].

We sort the jobs based on end time. -> O(NlogN)
Modify dp to be pairs of [e, total_profit], this would make find & insert easier.
The find & insert can be done by binary search. -> O(logN).
Overall time complexity: O(NlogN)

"""
class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s+1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])

        return dp[-1][1]

sol = Solution()
assert sol.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]) == 120
assert sol.jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]) == 150
assert sol.jobScheduling([1,1,1], [2,3,4], [5,6,4]) == 6
