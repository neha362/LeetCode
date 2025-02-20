#Construct Smallest Number From DI String, solved Feb 19 2025
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join(["0" if nums[i][i] == "1" else "1" for i in range(len(nums))])
