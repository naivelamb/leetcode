"""
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
#1 Brute force
Do two for-loop, check all possible XOR results.
Time Complexity O(n^2)

#2 Trie
XOR: 0^0 or 1^1 = 0; 1^0 or 0^1 = 1
For a given number, to get the maxium XOR, we need a number that is most complementary to it.

Get the binary string and pading the left part to a total length of 32. After insert the string, we try to find another string that is most complementary to it.

Time complexity: insert -> O(32), search -> O(32), overall -> O(32n)
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.value = 0

class Trie:
    def __init_(self):
        self.root = TrieNode()

    def insert(self, word, val):
        curr = self.root
        for i in range(len(word)):
            bit = word[i]
            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
        curr.isEnd = True
        curr.val = val

    def search(self, word, target):
        curr = self.root
        for i in range(len(word)):
            bit = word[i]

            if bit == '1' and curr.children.get('0'):
                curr = curr.children['0']
            elif bit == '0' and curr.children.get('1'):
                curr = curr.children['1']
            elif curr.children.get(bit):
                curr = curr.children[bit]
            else:
                break

        return target^curr.value

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        self.trie = Trie()
        max_xor = -2**(32)
        for i in nums:
            binary_string = (bin(i)[2:]).zfill(31)
            self.trie.insert(binary_string, i)
            max_xor = max(max_xor, self.trie.search(binary_string, i))

        return max_xor
