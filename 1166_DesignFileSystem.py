"""
https://leetcode.com/problems/design-file-system/
"""
class FileSystem:

    def __init__(self):
        self.ref = {"": -1}

    def createPath(self, path: str, value: int) -> bool:
        parent = '/'.join(path.split('/')[:-1])
        if parent in self.ref and path not in self.ref:
            self.ref[path] = value
            return True
        else:
            return False

    def get(self, path: str) -> int:
        return self.ref.get(path, -1)
