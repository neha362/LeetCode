#Minimum Value to Get Positive Step by Step Sum
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ret = 0
        sum = ret
        for i in nums: 
            sum += i
            ret = min(ret, sum)
        return 1 - ret
