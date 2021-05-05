"""
https://leetcode.com/problems/single-threaded-cpu/

Sort and use heap to manange pending task. 

Time complexity: O(nlogn)
"""
import collections

class Solution:
    def getOrder(self, tasks):
        ref = collections.defaultdict(list)
        for i, (t1, t2) in enumerate(tasks):
            ref[t1].append([t2, i])
        keys = sorted(ref.keys())[::-1]
        t, ans, pending = 0, [], []
        while True:
            if not keys and not pending:
                return ans
            if not pending:
                k = keys.pop()
                pending += ref[k]
                t = max(t, k)
            while keys and t >= keys[-1]:
                k = keys.pop()
                pending += ref[k]
            pending.sort(key=lambda x: (-x[0], -x[1]))
            #print(pending)
            if pending:
                t2, i = pending.pop()
                t += t2
                ans.append(i)
                

s = Solution()
print(s.getOrder(s3))