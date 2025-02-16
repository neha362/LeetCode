#Minimum Hours of Training to Win a Competition, solved Jan 16 2025
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        x = max(0, sum(energy) + 1 - initialEnergy)
        y = experience[0]
        z = 0
        for i in experience: 
            y = max(y, i - z)
            z += i
        return x + max(0, y - initialExperience + 1)

