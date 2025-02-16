# Minimum Number of Changes to Make Binary String Beautiful, solved Nov 4 2024
class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(0, len(s), 2): 
            if s[i:i + 2] != "00" and s[i:i + 2] != "11": 
                count += 1
        return count
        
