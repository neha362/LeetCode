#Max Sum of a Pair With Equal Sum of Digits, solved Feb 12 2025
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digitMap = [0] * 82
        res = -1
        for i in nums:
            count = 0
            j = i
            while j > 0:
                j, k = divmod(j, 10)
                count += k
            if digitMap[count] > 0:
                res = max(res, digitMap[count] + i)
            digitMap[count] = max(digitMap[count], i)
        return res
