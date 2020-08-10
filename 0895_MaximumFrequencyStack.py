"""
https://leetcode.com/problems/maximum-frequency-stack/

Use multiple stack to store data, the i-th stack stores the number for frequency i.

When push, we record the frequency, add to the corresponding stack, and update the max_freq. --> O(1)

When pop, we pop an element from the max_freq-th stack, update its frequency, remove the stack if it becomes empty, and update max_freq. --> O(1)

"""
class FreqStack:

    def __init__(self):
        self.stack_ = collections.defaultdict(list)
        self.freq = {}
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.freq[x] = self.freq.get(x, 0) + 1
        self.stack_[self.freq[x]].append(x)
        self.max_freq = max(self.max_freq, self.freq[x])

    def pop(self) -> int:
        ans = self.stack_[self.max_freq].pop()
        # update frequency
        self.freq[ans] -= 1
        if self.freq[ans] == 0:
            del self.freq[ans]
        # check stack
        if not self.stack_[self.max_freq]:
            del self.stack_[self.max_freq]
            self.max_freq -= 1
        return ans
