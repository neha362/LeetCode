# Check if Number is a Sum of Powers of Three, solved Mar 4 2025
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(15, -1, -1):
            print(n, 3 ** i)
            if n == 0:
                return True
            if n < 0:
                return False
            if 3 ** i > n:
                continue
            n -= 3 ** i
        return n == 0
