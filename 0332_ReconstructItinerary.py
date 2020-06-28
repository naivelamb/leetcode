"""
https://leetcode.com/problems/reconstruct-itinerary/
DFS. First build the graph. For every node, sort the possible destinations, try the destinations one-by-one, if dfs does not return True (faild to find a rounte), add destination back to the graph, remove it from route.

Time complexity: O(E^d), E ==> # of edges (flights), d ==> maximum number of connected nodes to a node (number of flights from an airport)
"""
class Solution:
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        for start, dst in tickets:
            graph[start].append(dst)

        route = ['JFK']
        def dfs(start='JFK'):
            if len(route) == len(tickets) + 1:
                return True
            dsts = sorted(graph[start])
            for dst in dsts:
                graph[start].remove(dst)
                route.append(dst)
                if dfs(dst):
                    return True
                graph[start].append(dst)
                route.pop()
        dfs()
        return route
