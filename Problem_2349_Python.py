#Design a Number Container System, solved Feb 8 2025
class NumberContainers:

    def __init__(self):
        self.nums = collections.defaultdict(SortedSet)
        self.indices = {}

    def change(self, index: int, number: int) -> None:
        if index in self.indices:
            prev = self.indices[index]
            self.nums[prev].remove(index)
            if not self.nums[prev]:
                del self.nums[prev]
        self.indices[index] = number
        self.nums[number].add(index)
        
    def find(self, number: int) -> int:
        if self.nums.__contains__(number) and self.nums[number]:
            return self.nums[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
