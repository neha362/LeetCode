#Unique Length-3 Palindromic Subsequences, solved Jan 9 2025
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        x = {chr(i): set({}) for i in range(ord("a"), ord("z") + 1)}
        count = 0
        for i in x: 
            if not s.__contains__(i):
                continue
            ind = s.index(i) + 1
            rind = s.rindex(i)
            x.get(i).update(s[ind:rind])
            count += len(x.get(i))
        return count
        
