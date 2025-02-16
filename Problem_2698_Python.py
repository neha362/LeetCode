#Find the Punishment Number of an Integer, solved Feb 15 2025
class Solution:
    def punishmentNumber(self, n: int) -> int:
        punishmentNum = 0
        for i in range(1, n + 1):
            x = i * i
            if self.canPartition(x, i):
                punishmentNum += x
        return punishmentNum

    def canPartition(self, num, target) -> bool:
        if target < 0 or num < target:
            return False
        if num == target:
            return True
        return self.canPartition(num//10, target - (num % 10)) or self.canPartition(num // 100, target - (num % 100)) or self.canPartition(num // 1000, target - (num % 1000))
