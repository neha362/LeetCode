#Construct Smallest Number From DI String, solved Feb 18 2025
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        x = len(pattern) + 1
        result = [-1] * x
        self.place([False] * x, pattern, 0, x, result)
        return "".join(str(i) for i in result)
        
    def place(self, used, pattern, index, end, result):
        print(used, pattern, index, end, result)
        if index == end:
            return True
        x = None
        if index == 0:
            x = range(1, end + 1)
        elif pattern[index - 1] == "D":
            x = range(1, result[index - 1])
        elif pattern[index - 1] == "I":
            x = range(result[index - 1] + 1, end + 1)
        for i in x:
            if used[i - 1]:
                continue
            result[index] = i
            used[i - 1] = True
            if self.place(used, pattern, index + 1, end, result):
                print("true", result)
                return True
            result[index] = -1
            used[i - 1] = False
        return False

            
