#Check if a Parentheses String Can Be Valid, solved Jan 12 2025
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1: 
            return False
        if (locked[0] == "1" and s[0] == ")") or (locked[-1] == "1" and s[-1] == "("):
            return False
        free = []
        stack = []
        diff = 0
        for i in range(len(s)): 
            if locked[i] == "0": 
                free.append(i)
            else:
                if s[i] == "(":
                    stack.append(i)
                else:
                    if stack:
                        stack.pop()
                    elif free: 
                        free.pop()
                    else: 
                        return False
        print(stack, free)
        for i in stack[::-1]: 
            if free and free[-1] > i: 
                free.pop()
                stack.pop()
            else: 
                return False
        return len(stack) <= len(free)
