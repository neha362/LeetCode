#Two Sum, solved Nov 5 2024
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if (len(nums) == 2): 
            return [0, 1]
        for i in range(len(nums)): 
            if nums[i + 1:].__contains__(target - nums[i]):
                return [nums[i + 1:].index(target - nums[i]) + i + 1, i]
        
