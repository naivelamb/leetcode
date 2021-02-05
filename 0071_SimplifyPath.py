"""
https://leetcode.com/problems/simplify-path/

Use a stack to maintain the directory, pop when see '..'.

Time complexity: O(N), N = # of file in the path
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for file in path:
            if file == '.' or not file:
                pass
            elif file == '..':
                if stack: stack.pop()
            else:
                stack.append(file)

        return '/' + '/'.join(stack)