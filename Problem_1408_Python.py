#String Matching in an Array, solved Jan 06 2025
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rep = set({})
        for i in range(len(words)): 
            for j in range(i + 1, len(words)):
                if len(words[i]) < len(words[j]) and words[j].__contains__(words[i]): 
                    rep.add(words[i])
                elif words[i].__contains__(words[j]): 
                    rep.add(words[j])
        return list(rep)
        
