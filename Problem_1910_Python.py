# Remove All Occurrences of a String, Feb 10 2025
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        y = len(part)
        while s.__contains__(part):
            x = s.index(part)
            s = s[:x] + s[x + y:]
            print(s)
        return s
        
