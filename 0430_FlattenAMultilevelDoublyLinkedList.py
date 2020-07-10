"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

DFS

"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        p0 = Node(None, None, head, None)

        def dfs(prev, curr):
            if not curr:
                return prev

            curr.prev = prev
            prev.next = curr
            tmpNext = curr.next
            tail = dfs(curr, curr.child)
            curr.child = None
            return dfs(tail, tmpNext)

        dfs(p0, head)
        p0.next.prev = None
        return p0.next
