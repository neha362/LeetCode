#Number of Ways to Split Array, Jan 3 2025
class Solution(object):
    def waysToSplitArray(self, nums):
        left = 0
        right = sum(nums)
        total = 0
        for i in range(len(nums) - 1): 
            left += nums[i]
            right -= nums[i]
            if left >= right:
                total += 1
                print(i)
        return total

        
        """
        :type nums: List[int]
        :rtype: int
        """
        
