# Climbing Stairs, solved Nov 5 2025
class Solution(object):
    def climbStairs(self, n):
        return int((5 ** -.5) * (((1 + 5**.5)/2) ** (n+1) - ((1 - 5**.5)/2) ** (n+1)))
        
