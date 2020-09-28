"""
https://leetcode.com/problems/evaluate-division/

Build graph based on the equations.
Search query.


"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        def build_graph(equations, values):
            def add_edge(a, b, value):
                if a in graph:
                    graph[a].append((b, value))
                else:
                    graph[a] = [(b, value)]

            for vertices, val in zip(equations, values):
                a, b = vertices
                add_edge(a, b, val)
                if val != 0:
                    add_edge(b, a, 1/val)

        def find(query):
            x, y = query
            if x not in graph or y not in graph:
                return -1

            #BFS to search
            q = collections.deque([(x, 1.0)])
            seen = set()
            while q:
                curr, curr_product = q.popleft()
                if curr == y:
                    return curr_product
                seen.add(curr)
                for nei, val in graph[curr]:
                    if nei not in seen:
                        q.append((nei, curr_product*val))
            return -1

        build_graph(equations, values)
        return [find(query) for query in queries]   
