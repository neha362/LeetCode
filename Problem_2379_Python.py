# Minimum Recolors to Get K Consecutive Black Blocks, solved Mar 7 2025
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # we first look at the first k blocks, looking at how many changes we have to make
        x = blocks[:k].count('W')
        y = x
        for i in range(k, len(blocks)):
            # we look at only the first and last blocks, seeing if there's a change to the minimum changes
            x = x + (1 if blocks[i] == 'W' else 0) - (1 if blocks[i - k] == 'W' else 0)
            y = min(x, y)
        #return the minimum number of changes
        return y
