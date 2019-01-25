# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/shopping-offers/

DFS with memorization 
Use memo to remember the lowest cost for a given needs. Needs -> tuple.
In the DFS, we first compute the cost of the needs without using any offers.
Then we try to use offer, if the offer is valid, we compute the new cost.
cost = min(cost, offer[-1] + dfs(_, _, new_need))
new_need -> new need if using the offer
"""

class Solution:
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        n = len(price)
        memo = {}
        def dfs(price, special, needs):
            # needs -> tuple
            # return minimum cost for a given needs
            if needs in memo:
                return memo[needs]
            # cost without using offer
            cost = sum([price[i]*needs[i] for i in range(n)])
            # try using offer
            for offer in special:
                for i in range(n):
                    if needs[i] - offer[i] < 0:
                        break
                else:
                    new_needs = tuple(needs[i] - offer[i] for i in range(n))
                    cost = min(cost, dfs(price, special, new_needs) + offer[-1])
            memo[needs] = cost
            return cost
        return dfs(price, special, tuple(needs))

price = [2, 5]
special = [[3, 0, 5], [1, 2, 10]]
needs = [3, 2]
s = Solution()
print(s.shoppingOffers(price, special, needs))