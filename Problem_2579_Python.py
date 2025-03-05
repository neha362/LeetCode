# Count Total Number of Colored Cells, solved Mar 4 2025
class Solution:
    def coloredCells(self, n: int) -> int:
        return n ** 2 + (n - 1) ** 2
