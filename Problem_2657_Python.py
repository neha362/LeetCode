# Find the Prefix Common Array of Two Arrays, solved 
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        x = [1 for i in range(len(A))]
        y = []
        if (A[0] == B[0]):
            y.append(1)
        else: 
            y.append(0)
        x[A[0] - 1] = 0
        x[B[0] - 1] = 0
        for i in range(1, len(A)): 
            if A[i] == B[i]:
                y.append(y[-1] + 1)
            else: 
                y.append(y[-1] + (1 if x[A[i] - 1] == 0 else 0) + (1 if x[B[i] - 1] == 0 else 0))
            x[A[i] - 1] = 0
            x[B[i] - 1] = 0
        return y
        

        
