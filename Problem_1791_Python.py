#Find Center of a Star Graph, solved Nov 9 2024
class Solution(object):
    def findCenter(self, edges):
        x = edges[0] + edges[1]
        for i in x:
            if (x.count(i) == 2):
                return i
        return null
        
