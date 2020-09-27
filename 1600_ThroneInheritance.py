"""
https://leetcode.com/problems/throne-inheritance/

Build the graph, do in-order tranverse when get inheritance order.

Time Complexity: O(N)
"""
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = collections.defaultdict(list)
        self.root = kingName
        self.deaths = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def dfs(node, ans):
            if node not in self.deaths:
                ans.append(node)
            for child in self.graph[node]:
                dfs(child, ans)

        dfs(self.root, ans)
        return ans
