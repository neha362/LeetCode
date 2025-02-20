#The k-th Lexicographical String of All Happy Strings of Length n
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 2 ** (n - 1):
            return ""
        string = [""] * n
        self.find(n, [k], string, 0, ["a", "b", "c"])
        return "".join(string)
    
    def find(self, n, k, string, index, letters):
        if index == n and k[0] == 1:
            return True
        if index == n:
            k[0] -= 1
            return False
        for i in letters:
            if index != 0 and string[index - 1] == i:
                continue
            string[index] = i
            if self.find(n, k, string, index + 1, letters):
                return True
            string[index] = ""
        return False
