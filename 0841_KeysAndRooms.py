"""
https://leetcode.com/problems/keys-and-rooms/

DFS
Try to enter every room.

Time complexity: O(N)
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        entered_room = set()
        n = len(rooms)
        stack = [0]
        while stack:
            room = stack.pop()
            if room in entered_room:
                continue
            entered_room.add(room)
            stack += rooms[room]

        return n == len(entered_room)