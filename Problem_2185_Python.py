#Counting Words with a Given Prefix, solved Jan 9 2025
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in words: 
            count += 1 if i[:len(pref)] == pref else 0
        return count
