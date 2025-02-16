#Minimize XOR, solved Jan 15 2025
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        x = bin(num2).count("1")
        diff = x - bin(num1).count("1")
        y = list(bin(num1)[2:])
        print(y, x)
        if num2 > num1: 
            for i in range(len(bin(num2)) - len(bin(num1))):
                y.insert(0, "0")
        print(y, diff)
        for i in range(diff):
            y[len(y) - 1 - y[::-1].index("0")] = "1"
        for i in range(-1 * diff):
            y[len(y) - 1 - y[::-1].index("1")] = "0"
        print(y)
        return int("".join(y), 2)

        
