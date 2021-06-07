"""
https://leetcode.com/problems/open-the-lock/

BFS

"""
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        ref = {
            '0': ['1', '9'],
            '1': ['0', '2'],
            '2': ['1', '3'],
            '3': ['2', '4'],
            '4': ['3', '5'],
            '5': ['4', '6'],
            '6': ['5', '7'],
            '7': ['6', '8'],
            '8': ['7', '9'],
            '9': ['8', '0'],
        }
        queue = collections.deque([['0000', 0]])
        deadends = set(deadends)
        visited.add('0000')
        if '0000' in deadends:
            return -1
        while queue:
            node, step = queue.popleft()
            if node == target:
                return step
            for i, ch in enumerate(node):
                for new_ch in ref[ch]:
                    new_node = node[:i] + new_ch + node[i+1:]
                    if new_node == target:
                        return step + 1
                    if new_node not in visited and new_node not in deadends:
                        queue.append([new_node, step + 1])
                        visited.add(new_node)
        return -1
                