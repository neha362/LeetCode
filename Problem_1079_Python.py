#Letter Tile Possibilities, solved Feb 17 2025
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = "".join(sorted(tiles))
        return int(self.count(tiles, 0, len(tiles), set()))

    def count(self, tiles, index, end, seen):
        if index == end:
            if tiles in seen:
                return 0
            seen.add(tiles)
            x = {i:tiles.count(i) for i in tiles}
            total, product = 0, 1
            for i in x:
                if i != 0: 
                    total += x[i]
                    product *= math.factorial(x[i])
            if total == 0:
                return 0
            return math.factorial(total)/product
        return self.count(tiles, index + 1, end, seen) + self.count(tiles[:index] + tiles[index + 1:], index, end - 1, seen)
