"""
https://leetcode.com/problems/get-watched-videos-by-your-friends/

BFS to find the kth level friends, count the movies, sort them.
"""
class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, id: int, level: int):
        current_level = 0
        curr_friends = [id]
        lower_level_friends = set()
        lower_level_friends.add(id)
        while curr_friends and current_level < level:
            new_friends = []
            for idx in curr_friends:
                temp_friends = friends[idx]
                for f in temp_friends:
                    if f not in lower_level_friends:
                        new_friends.append(f)
                        lower_level_friends.add(f)
            current_level += 1
            curr_friends = new_friends

        cnt = {}
        for f in curr_friends:
            for v in watchedVideos[f]:
                cnt[v] = cnt.get(v, 0) + 1

        ans = [(cnt[k], k) for k in cnt.keys()]
        ans.sort()
        return [x[1] for x in ans]
