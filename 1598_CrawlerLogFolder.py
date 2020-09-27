"""
https://leetcode.com/problems/crawler-log-folder/

Use tree to store the structure.
Time Complexity: O(N), N = len(logs)
"""

class Node:
    def __init__(self):
        self.level = 0
        self.parent = None
        self.children = {}

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        curr = Node()
        for log in logs:
            if log == '../':
                if curr.level == 0:
                    curr = curr
                else:
                    curr = curr.parent
            elif log == './':
                curr = curr
            else:
                sub = Node()
                sub.level = curr.level + 1
                curr.children[log] = sub
                sub.parent = curr
                curr = sub
        return curr.level
