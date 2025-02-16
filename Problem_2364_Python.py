#Count Number of Bad Pairs, solved Feb 10 2025
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        x = {}
        y = len(nums)
        for i in range(y):
            if i - nums[i] in x:
                x[i-nums[i]] += 1
            else:
                x[i-nums[i]] = 1
        count = y * (y - 1)/2
        for i in x:
            count -= x[i] * (x[i] - 1)/2
        return int(count)
            
