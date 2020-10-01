"""
https://leetcode.com/problems/number-of-recent-calls/

Use queue to store the ping time stamp. Pop those item < (t-3000) when ping.

Time Comcomplexity: O(N)
"""
class RecentCounter:

    def __init__(self):
        self.queue = collections.deque([])
        self.n = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.n += 1
        while self.queue[0] < t - 3000:
            self.queue.popleft()
            self.n -= 1
        return self.n


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
