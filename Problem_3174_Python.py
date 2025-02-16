#Clear Digits, solved Feb 10 2025
class Solution:
    def clearDigits(self, s: str) -> str:
        string = ""
        for i in s: 
            if i.isnumeric():
                string = string[:-1]
            else:
                string += i
        return string
        
        
