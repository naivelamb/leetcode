"""
https://leetcode.com/problems/candy/

dp + greedy. 

Go from the left, find the rank of each position, rank_l. 
Go from the right, find the rank of each position, rank_r. 

For child-i, the candies given to him is max(rank_l[i], rank_r[i])

Time complexity: O(N)
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        dp_l, dp_r = [1], [1]
        n = len(ratings)
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                dp_l.append(dp_l[-1] + 1)
            else:
                dp_l.append(1)
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                dp_r.append(dp_r[-1] + 1)
            else:
                dp_r.append(1)
        dp_r = dp_r[::-1]

        ans = 0
        for i in range(n):
            ans += max(dp_l[i], dp_r[i])
        return ans