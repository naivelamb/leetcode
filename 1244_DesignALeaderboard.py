"""
https://leetcode.com/problems/design-a-leaderboard/

Use a hash map to store the information. When getting top K, first get all scores,
then heapify it, finally pop out K elements.

Time complexity:
addScore() -> O(1)
top() -> O(N + Klog(N))
reset() -> O(1)
where N is the total player number.
"""
class Leaderboard:

    def __init__(self):
        self.score = {}

    def addScore(self, playerId, score):
        if playerId in self.score:
            self.score[playerId] += score
        else:
            self.score[playerId] = score

    def top(self, K):
        scores = [- x for x in self.score.values()]
        heapq.heapify(scores)
        i, ans = 0, 0
        while i < K:
            ans -= heapq.heappop(scores)
            i += 1
        return ans

    def reset(self, playerId):
        self.score[playerId] = 0



# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
