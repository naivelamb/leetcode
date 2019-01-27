# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/time-based-key-value-store/

The set operation is in strict ascending order, so we can use binary search to 
do get. 

Time complexity:
Set: O(1)
Get: O(logn)
"""
import bisect
import collections
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ref = collections.defaultdict(list)
        self.times = collections.defaultdict(list)

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        self.ref[key].append(value)
        self.times[key].append(timestamp)

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        times = self.times[key]
        vals = self.ref[key]
        if not vals:
            return ''
        if timestamp < times[0]:
            return ''
        if timestamp >= times[-1][0]:
            return vals[-1]
        idx = bisect.bisect(times, timestamp)
        return vals[idx-1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
