#Number of Common Factors, Jan 16 2025
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        l = 1
        n = 0
        e = 2
        while a != 1 and b != 1 and e <= a and e <= b:
            while a % e == 0 and b % e == 0: 
                n += 1
                a /= e
                b /= e
                print(e)
            e += 1
            l *= n + 1
            n = 0
        return l
