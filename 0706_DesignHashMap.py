"""
https://leetcode.com/problems/design-hashmap/

Use linked list to implement it. Each bucket stores a linked list, where each node stores (key, value) pair.

When put/get/remove, first find the bucket, then go through the linked list to append/find/delete the element. 

Space complexity: O(1000)
Time complexity: O(1000)
"""
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = [None] * self.size


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size

        if self.table[index] is None:
            self.table[index] = ListNode(key, value)
        else:
            cur = self.table[index]
            while True:
                if cur.key == key:
                    cur.value = value
                    return
                if cur.next is None:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        cur = self.table[index]
        while cur:
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        cur = prev = self.table[index]
        if not cur:
            return
        if cur.key == key:
            self.table[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.key == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)