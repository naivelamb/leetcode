"""
https://leetcode.com/problems/prefix-and-suffix-search/

For each word, insert all its [suffix + '#' + word] in to the trie. Then for a pair for [prefix, suffix], we just need to search [suffix + '#' + prefix].

Time complexity: O(NK^2 + QK)
where N is number of words, K is the maximum length of a word, Q is the number of query. 
"""
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = False

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()

        for weight, word in enumerate(words):
            word += '#'
            for i in range(len(word)):
                cur = self.trie
                cur[WEIGHT] = weight
                for j in range(i, 2*len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[WEIGHT] = weight

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for letter in suffix + '#' + prefix:
            if letter not in cur:
                return -1
            cur = cur[letter]

        return cur[WEIGHT]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)