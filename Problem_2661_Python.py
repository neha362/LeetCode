#First Completely Painted Row or Column, solved Jan 20 2025
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row_l = len(mat)
        col_l = len(mat[0])
        x = {mat[i][j]: (i, j) for i in range(row_l) for j in range(col_l)}
        rows = [col_l for i in range(row_l)]
        cols = [row_l for j in range(col_l)]
        for i in range(len(arr)): 
            if rows[x[arr[i]][0]] == 1 or cols[x[arr[i]][1]] == 1:
                return i
            rows[x[arr[i]][0]] -= 1
            cols[x[arr[i]][1]] -= 1
        return -1
