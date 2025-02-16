#Product of the Last K Numbers, solved Feb 14 2025
class ProductOfNumbers:
    def __init__(self):
        self.lst = []

    def add(self, num: int) -> None:
        self.lst.append(num)

    def getProduct(self, k: int) -> int:
        return math.prod(self.lst[-1 * k:])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
