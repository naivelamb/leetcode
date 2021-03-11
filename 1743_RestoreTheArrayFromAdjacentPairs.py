"""
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

Build the bi-directional graph based on pairs. While building the graph, record node frequency, the two with only one appearance is the potential head.
Then DFS from either head.

Time compleixty: O(e + v)
"""
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # build graph and find head
        head = set()
        graph = collections.defaultdict(list)
        for x, y in adjacentPairs:
            head.remove(x) if x in head else head.add(x)
            head.remove(y) if y in head else head.add(y)
            graph[x].append(y)
            graph[y].append(x)
        
        # DFS
        stack, ans, seen = [], [], set()
        stack.append(list(head).pop())
        while stack:
            node = stack.pop()
            ans.append(node)
            seen.add(node)
            for next_node in graph[node]:
                if next_node not in seen:
                    stack.append(next_node)
        return ans

        