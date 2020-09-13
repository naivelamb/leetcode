"""
https://leetcode.com/problems/insert-interval/

Use an array to store the answer.
Compare the last element of the answer array and the current one in the intervals, do one of the following operations:
1. merge, then append. ==> overlap
2. append the two intervals in sorted order. ==> non-overlap

Time Complexity: O(N), N = len(intervals)

"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]

        ans = []
        prev = newInterval
        for interval in intervals:
            if prev[0] <= interval[0] <= prev[1] or interval[0] <= prev[0] <= interval[1]:
                new_interval = self.merge(prev, interval)
                ans.append(new_interval)
            else:
                if interval[1] < prev[0]:
                    ans.append(interval)
                    ans.append(prev)
                else:
                    ans.append(prev)
                    ans.append(interval)
            prev = ans.pop()
        ans.append(prev)
        return ans

    def merge(self, l1, l2):
        start = min(l1[0], l2[0])
        end = max(l1[1], l2[1])
        return [start, end]
