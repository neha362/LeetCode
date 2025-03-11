# Number of Substrings Containing All Three Characters, solved Mar 11 2025
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # uses a sliding window approach similar to previous day's strategy
        count, start, end = 0, 0, 0
        # since there are only three options, keeps track using a dict
        vals = {'a': 0, 'b':0, 'c':0}
        while end < len(s):
            vals[s[end]] += 1
            while vals['a'] > 0 and vals['b'] > 0 and vals['c'] > 0:
                count += len(s) - end
                vals[s[start]] -= 1
                start += 1
            end += 1
        return count
