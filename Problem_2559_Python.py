#Count Vowel Strings in Ranges, solved Jan 9 2025
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        x = [vowels.get(words[0][0], 0) * vowels.get(words[0][-1], 0)]
        for i in words[1:]: 
            x.append(vowels.get(i[0], 0) * vowels.get(i[-1], 0) + x[-1])
        print(x)
        return [x[i[1]] - x[i[0] - 1] if i[0] > 0 else x[i[1]] for i in queries] 

        
