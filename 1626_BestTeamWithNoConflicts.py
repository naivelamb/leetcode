"""
https://leetcode.com/problems/best-team-with-no-conflicts/

Sort the array [(age, score)], therefore we don't need to check ages and scores together. As long as the scores a in increasing order, we are find. 
Let dp[i] be the maximum score that can be obtrained when i-th palyer is included and all players in [0, i-1]. 

Time complexity: O(nlogn + n^2)
"""
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_score = list(zip(ages, scores))
        age_score.sort()

        ages = [x[0] for x in age_score]
        scores = [x[1] for x in age_score]

        n = len(scores)
        dp = [0] * n
        for i in range(n):
            dp[i] = scores[i]
            for j in range(i):
                if scores[j] <= scores[i]:
                    dp[i] = max(dp[i], dp[j] + scores[i])
        return max(dp)