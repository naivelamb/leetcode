"""
https://leetcode.com/problems/task-scheduler/

Find the most frequent tasks, place them first, then fill the "empty" slot (n-1) with other tasks.

Time Complexity: O(N), N=len(tasks)
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        most_freq = 0
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
            most_freq = max(most_freq, freq[task])

        cnt = 0
        for key in freq:
            if freq[key] == most_freq:
                cnt += 1

        ans = (most_freq - 1) * (n + 1) + cnt
        return max(ans, len(tasks))
