#Maximum Score After Splitting a String, solved Jan 9 2025
class Solution:
    def maxScore(self, s: str) -> int:
        t = [1 - int(s[0])]
        for i in s[1:-1]: 
            t.append(t[-1] + (1 if i == "0" else -1))
            print(i, t)
        x = t.index(max(t)) + 1
        print(x)
        return s[:x].count("0") + s[x:].count("1")
