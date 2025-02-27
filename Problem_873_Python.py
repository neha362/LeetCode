# Length of Longest Fibonacci Subsequence, solved 2/27/2025
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_val, val = 0, 0
        seen = set(arr)
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                max_val = max(max_val, val)
                val = 0
                x, y = arr[i], arr[j]
                while (x + y) in seen:
                    print(x, y, x + y)
                    temp = x
                    x = y
                    y = temp + x
                    val += 1
        print(seen)
        return max_val + 2 if max_val != 0 else 0
