# Alternating Groups II, solved Mar 8 2025
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # keep these as variables to keep runtime costs low
        length = len(colors)
        count = 0
        x = 0
        # cycle through the list, keeping track of how many consecutive blocks we've seen
        for i in range(length + k - 1):
            if colors[i % length] == colors[(i + 1) % length]:
                # if count was k, we can add another string before we reset
                if count == k - 1:
                    x += 1
                count = 0
            else:
                # keep increasing count, keeping k as the upper bound
                count += 1
                if count == k:
                    x += 1
                    count -= 1
        # return the number of times count touched k
        return x

