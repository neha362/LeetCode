# Find Missing and Repeated Values, solved Mar 5 2025
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
      #initialize a default dict that returns 0
        x = collections.defaultdict(int)
      #the sum of the values in the grid (if every value is counted once) is n ^ 2 ( n ^ 2 + 1) / 2, 
      #so we subtract the value that occurs twice to find the difference between a and b
        y, z = (0, len(grid)**2 * (len(grid)**2 + 1)//2)
        for i in grid:
            for j in i:
                z -= j
              #assign y if this is the second time we are seeing a value
                if x[j] == 1:
                    y = j
                    continue
                x[j] = 1
              #return the tuple
        return (y, y + z)
