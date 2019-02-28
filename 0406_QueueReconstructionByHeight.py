# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/queue-reconstruction-by-height/

#1 Greedy
We know where to put the shortest guy, ans[k].
Then for the next shortest guy, we need to put him at the k-th empty slot. 
Time complexity: O(nlogn + n^2)

#2 Insert order
We can start the procedure from the tallest people. Take 
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]] 
as an example, for people of height 7, we know that,
[[7, 0], [7, 1]] 
Then [6, 1] is inserted at location 1. 
[[7, 0], [6, 1], [7, 1]]
And we keep this process going until all people is placed. 
Time Complexity: O(nlogn + n^2)
"""
class Solution:
    def reconstructQueue_greedy(self, people):
        n = len(people)
        ans = [0] * n
        people.sort(reverse=True)
        while people:
            p = people.pop()
            i, cnt = 0, 0
            while cnt <= p[1]:
                if ans[i] == 0: #empty:
                    cnt += 1
                elif ans[i][0] >= p[0]:
                    cnt += 1
                i += 1
            ans[i - 1] = p
        return ans

    def reconstructQueue_insert(self, people):
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res   