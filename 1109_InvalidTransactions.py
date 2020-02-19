"""
https://leetcode.com/problems/invalid-transactions/
"""
class Transaction():
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city

class Solution:
    def invalidTransactions(self, transactions):
        transactions = [Transaction(*transaction.split(',')) for transaction in transactions]
        transactions.sort(key = lambda t: t.time)

        trans_indexes = {}
        for i, t in enumerate(transactions):
            trans_indexes[t.name] = trans_indexes.get(t.name, []) + [i]

        res = []
        for name, indexes in trans_indexes.items():
            left = right = 0
            for i, t_index in enumerate(indexes):
                t = transactions[t_index]
                if t.amount > 1000:
                    res.append("{},{},{},{}".format(t.name, t.time, t.amount, t.city))
                    continue
                while left <= len(indexes) - 2 and transactions[indexes[left]].time < t.time - 60:
                    left += 1
                while right <= len(indexes) - 2 and transactions[indexes[right+1]].time <= t.time + 60:
                    right += 1
                for i in range(left, right+1):
                    if transactions[indexes[i]].city != t.city:
                        res.append("{},{},{},{}".format(t.name, t.time, t.amount, t.city))
                        break

        return res

sol = Solution()
transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
assert sol.invalidTransactions(transactions) == ["alice,20,800,mtv","alice,50,100,beijing"]
transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
assert sol.invalidTransactions(transactions) == ["alice,50,1200,mtv"]
transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
assert sol.invalidTransactions(transactions) == ["bob,50,1200,mtv"]
