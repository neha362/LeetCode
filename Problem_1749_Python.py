#Maximum Absolute Sum of Any Subarray, solved Feb 25 2025
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr, max_val, min_val = 0, 0, 0
        for i in nums:
            curr += i
            if curr > max_val:
                max_val = curr
            if curr < min_val:
                min_val = curr
        return max_val - min_val
