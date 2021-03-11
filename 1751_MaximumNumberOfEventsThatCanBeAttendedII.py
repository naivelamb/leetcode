"""
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

To make search easier, we need to sort the events based on starting point. Hence if we decide to attend one event, it is easily to find next available event to attend.

dp(i, k) gives maximum value if starts with event i with at most k event to attend. 

dp(i, k) = max(dp(i + 1, k), events[i][2] + dp(next_event, k - 1))

next_event can be acheived by binary search.

Time complexity: O(nlogn + nklogn) => O(nklogn)

"""
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [x for x, _, _ in events]

        @lru_cache(None)
        def dp(i, k):
            if k == 0 or i >= len(events):
                return 0
            next_event = bisect_right(starts, events[i][1])
            return max(dp(i+1, k), events[i][2] + dp(next_event, k-1))
        
        return dp(0, k)