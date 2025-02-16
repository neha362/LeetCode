#Kids with the Greatest Number of Candies, solved Oct 14 2024
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        return [(i + extraCandies) >= maxCandies for i in candies]
        
