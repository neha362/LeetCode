#Neighboring Bitwise Or, solved Jan 16 2025
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        x = 0
        for i in derived: 
            x = x ^ i
        return x == 0
