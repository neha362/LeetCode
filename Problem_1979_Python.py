#Find Greatest Common Divisor of Array, solved Oct 12 2024
class Solution(object):
    def findGCD(self, nums):
        max_val = max(nums)
        min_val = min(nums)
        while(max_val >= 0 and min_val >= 0): 
            if (max_val % min_val == 0):
                return min_val
            if (max_val > min_val):
                max_val -= min_val
            if (min_val > max_val):
                min_val -= max_val
        return 1
        
