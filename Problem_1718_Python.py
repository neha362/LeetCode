#Construct the Lexicographically Largest Valid Sequence, solved Feb 16 2025
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        #if each value is counted twice except for 1, which is counted once, there are 2n - 1 values in the array
        x = [0] * (2 * n - 1)
        self.canPlace(0, x, [False] * n, n)
        return x
    
    #recursive helper function
    def canPlace(self, index, result, isUsed, target):
        if index == len(result):
            return True
        if result[index] != 0:
            return self.canPlace(index + 1, result, isUsed, target)
        for i in range(target, 0, -1):
            if isUsed[i - 1]:
                continue
            result[index] = i
            isUsed[i - 1] = True
            if i == 1:
                if self.canPlace(index + 1, result, isUsed, target):
                    return True
            elif index + i < len(result) and result[index + i] == 0:
                result[index + i] = i
                if self.canPlace(index + 1, result, isUsed, target):
                    return True
                result[index + i] = 0
            isUsed[i - 1] = False
            result[index] = 0
        return False
