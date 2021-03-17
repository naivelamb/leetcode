"""
https://leetcode.com/problems/count-items-matching-a-rule/

Hash ruleKey and position, go through item.
Time complexity: O(N)
"""
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx = {'type':0, 'color':1, 'name': 2}
        ans = 0
        for v in items:
            if v[idx[ruleKey]] == ruleValue:
                ans += 1
        return ans