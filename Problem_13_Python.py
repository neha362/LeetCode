#Roman to Integer, Nov 5 2024
class Solution(object):
    def romanToInt(self, s):
        total = 0
        x = {'I':1, 'V': 5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s) - 1): 
            if (x.get(s[i]) < x.get(s[i + 1])): 
                total -= x.get(s[i])
            else: 
                total += x.get(s[i])
        return total + x.get(s[len(s) - 1])
        
