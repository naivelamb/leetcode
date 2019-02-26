# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/exam-room/

#1 Naive Solution
Maintain a sorted list of seated student. 
The maximum position can be computed by one scan. 
Remove is just list.remove(p). 
Time Complexity: Both are O(n)


#2 Heap + dict
We use heap to maintain the current (intervals length, start, end).
Let's say we have the information about an empty site and its neighbors, left and right.
Once the empty site is occupied, we need to set, 
Its left's right neighbor to be the empty site.
Its right's left neighbor to be the empty site.
We also generate two new intervals, which need to be pushed into the heap.

When leave, we need to combine two intervals and update the neighbor information.

We can use two dictionaries to maintain the neighbor information. 
We don't need to delete an intervals, an popped intervals is valid only when
its neighbors information matches its start and end.
"""
import bisect
class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.students = [] #students that seat. 

    def seat(self) -> int:
        if not self.students:
            student = 0
        else:
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    if (s - prev) // 2 > dist:
                        dist, student = (s - prev) // 2, (s + prev) // 2
            if self.N - 1 - self.students[-1] > dist:
                dist, student = self.N - 1 - self.students[-1], self.N - 1
        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)

import collections
import heapq
class ExamRoom_heap:

    def __init__(self, N: int):
        self.n = N
        self.heap = []
        self.right = collections.defaultdict(int)
        self.left = collections.defaultdict(int)
        self.push(0, self.n - 1)
        
    def push(self, l, r):
        # push an interval to the heap
        if r >= l:
            width = -((r - l)//2) # -5//2 = -3, -(5//2) = 2
            if l == 0 or r == self.n - 1:
                width = l - r
            self.right[l] = r
            self.left[r] = l
            heapq.heappush(self.heap, (width, l, r))
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        w, l, r = heapq.heappop(self.heap)
        if not self.right[l] == r:
            # keep popping untill valid 
            return self.pop()
        return (w, l, r)
        
    def seat(self) -> int:
        w, l, r = self.pop()
        t = l + (r - l) // 2
        if l == 0:
            t = 0
        elif r == self.n-1:
            t = r
        self.push(l, t - 1)
        self.push(t + 1, r)
        self.left[t] = -1
        self.right[t] = -1
        return t
        
    def leave(self, p: int) -> None:
        l, r = None, None
        if p == 0:
            l = 0
        else:
            if self.left[p - 1] != -1:
                l = self.left[p - 1]
            else:
                l = p
        if p == self.n - 1:
            r = self.n - 1
        else:
            if self.right[p + 1] != -1:
                r = self.right[p + 1]
                self.right[p + 1] = 0
            else:
                r = p
        self.push(l, r)
