#Number of Sub-arrays With Odd Sum, solved Feb 24 2025
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        val, y = 0, 0
        for i in arr:
            val += i
            y += val % 2
        return (y + y * (len(arr) - y)) % (10 ** 9 + 7)
