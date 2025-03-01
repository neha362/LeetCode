# Apply Operations to an Array, solved Mar 1 2025
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        new_nums = [0] * len(nums)
        ind = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if i < len(nums) - 1 and nums[i] == nums[i + 1] and nums[i]:
                new_nums[ind] = nums[i] * 2
                nums[i + 1] = 0
                ind += 1
            elif nums[i] != 0:
                new_nums[ind] = nums[i]
                ind += 1
        return new_nums
