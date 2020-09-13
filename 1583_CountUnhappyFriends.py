"""
https://leetcode.com/problems/count-unhappy-friends/

Brute force. Store perference in a dictionary.
Time Complexity: O(n^2)
"""
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        ref = collections.defaultdict(dict)
        for i in range(n):
            for j, p in enumerate(preferences[i]):
                ref[i][p] = j

        ref_pair = {}
        for i, j in pairs:
            ref_pair[i] = j
            ref_pair[j] = i

        ans = set()
        for x in range(n):
            y = ref_pair[x]
            if ref[x][y] != 0:
                # check better friends
                for u in preferences[x][:ref[x][y]]:
                    v = ref_pair[u]
                    if ref[u][x] < ref[u][v]:
                        ans.add(x)
                        break
        return len(ans)
