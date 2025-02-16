#Word Subsets, Jan 10 2025
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        x = {}
        for i in words2: 
            for j in i: 
                if (x.__contains__(j)):
                    x.update({j: max(x.get(j), i.count(j))})
                else:
                    x.update({j:i.count(j)})
        t = []
        for i in words1: 
            y = True
            for j in x: 
                if (i.count(j) < x.get(j)):
                    print(i, j, x.get(j))
                    y = False
                    continue
            if y: 
                t.append(i)
        return t

        
