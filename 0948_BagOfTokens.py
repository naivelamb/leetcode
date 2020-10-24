"""
https://leetcode.com/problems/bag-of-tokens/

We can do the token in any order. The best way would be try to use up points to get as many scores as possible, then use one scores to get most points, then do it again. 

This is a greedy process. We need to have a sorted token array. 

Time complexity: O(NlogN)
"""
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        deque = collections.deque(sorted(tokens))
        ans = score = 0

        while deque and (P >= deque[0] or score >= 1):
            # first use points as many as possible
            while deque and P >= deque[0]:
                P -= deque.popleft()
                score += 1
            ans = max(score, ans)

            # get points
            if deque and score >= 1:
                P += deque.pop()
                score -= 1
        
        return ans