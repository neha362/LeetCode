#Reverse Vowels of a String, solved Jan 16 2025
class Solution:
    def reverseVowels(self, s: str) -> str:
        x = 0
        y = len(s) - 1
        while (y > x):
            if "AEIOUaeiou".__contains__(s[x]):
                if "AEIOUaeiou".__contains__(s[y]):
                    s = s[:x] + s[y] + s[x + 1: y] + s[x] + s[y + 1:]
                    x += 1
                    y -= 1
                else:
                    y -= 1
            else: 
                x += 1
        return s
