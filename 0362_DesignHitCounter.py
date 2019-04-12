# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/design-hit-counter/

Use deque to keep track of timestamp and hits received at that time. 
hit() append record.
getHits() popleft record that expires.

Time complexity: hit() -> O(1), getHits() -> O(s), s = len(self.hits) 
"""
import collections
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = collections.deque([])
        self.hits = collections.deque([])
        self.total = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hits.append(1)
        self.times.append(timestamp)
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.times and timestamp - self.times[0] >= 300:
            self.times.popleft()
            self.total -= self.hits.popleft()
        return self.total
