#Construct K Palindrome Strings, solved Jan 11 2025
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        y = set()
        y.update(s)
        if len(s) < k:
            return False
        if len(s) == k: 
            return True
        for x in y: 
            if k < 0: 
                return False
            if s.count(x) % 2 == 1: 
                k -= 1
                print(x)
        if (k < 0):
            return False
        return True


        
