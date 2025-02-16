#Minimum Length of String After Operations, solved Jan 13 2025
class Solution:
    def minimumLength(self, s: str) -> int:
        return sum([2 - s.count(i) % 2 for i in set(s)])
