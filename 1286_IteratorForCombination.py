"""
https://leetcode.com/problems/iterator-for-combination/
compute all the combinations in __init__, then just do iterations.

Time complexity:
__init__: O(K), K = C(N, combinationLength), N = len(characters)
next: O(1)
hasNext: O(1)
"""
class CombinationIterator:
    def combine(self, characters, ind, combinationLength, ans):
        if combinationLength == 0:
            self.combinations.append(ans[:])
            return
        for i in range(ind, len(characters)):
            self.combine(characters, i+1, combinationLength-1, ans+characters[i])


    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self.combine(characters, 0, combinationLength, '')
        self.i = 0

    def next(self) -> str:
        value = self.combinations[self.i]
        self.i += 1
        return value

    def hasNext(self) -> bool:
        if self.i >= len(self.combinations):
            return False
        return True
