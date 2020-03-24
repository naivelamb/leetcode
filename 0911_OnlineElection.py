"""
https://leetcode.com/problems/online-election/

Pre compute the result in __init__(), time complexity: O(N), N = len(times)
For query, do binary search. Time complexity for one query: O(logN)

Overall time complexity: O(N + QlogN), Q = # of queries
"""
class TopVotedCandidate:

    def __init__(self, persons, times):
        self.ans = []
        count = {}
        leader, votes = None, 0
        for p, t in zip(persons, times):
            count[p] = count.get(p, 0) + 1
            c = count[p]
            if c >= votes:
                if p != leader: # change leader
                    leader = p
                    self.ans.append((t, leader))
                votes = c

    def q(self, t: int) -> int:
        i = bisect.bisect(self.ans, (t, float('inf')), 1)
        return self.ans[i-1][1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
