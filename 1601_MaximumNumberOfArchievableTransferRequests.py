"""
https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

Try all combinations.

Time complexity: O(k*2^n)
n = len(requests)
k = # of buildings
"""
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def helper(idxs, requests, n):
            cnt = [0] * n
            for i in idxs:
                a, b = requests[i]
                cnt[a] -= 1
                cnt[b] += 1
            return all(x == 0 for x in cnt)

        ans = len(requests)
        all_idx = list(range(ans))
        while ans > 0:
            idxs_list = list(itertools.combinations(all_idx, ans))
            for idxs in idxs_list:
                if helper(idxs, requests, n):
                    return ans
            ans -= 1
        return -1
