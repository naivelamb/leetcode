"""
https://leetcode.com/problems/apply-discount-every-n-orders/
"""
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.N = n
        self.n = 0
        self.discount = (100 - discount)/100
        self.price_map = {}
        for prod, price in zip(products, prices):
            self.price_map[prod] = price

    def getBill(self, product, amount) -> float:
        price = 0
        for prod, cnt in zip(product, amount):
            price += self.price_map[prod] * cnt

        self.n += 1
        if self.n == self.N:
            price *= self.discount
            self.n = 0
        return price


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

sol = Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100])
assert sol.getBill([1,2],[1,2]) == 500
assert sol.getBill([3,7],[10,10]) == 4000
assert sol.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]) == 800
assert sol.getBill([4],[10]) == 4000
assert sol.getBill([7,3],[10,10]) == 4000
assert sol.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]) == 7350
assert sol.getBill([2,3,5],[5,3,2]) == 2500
