#Circular Sentence, solved Nov 8 2024
class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        x = sentence.rsplit(" ")
        for i in range(len(x)):
            if (i == len(x) - 1):
                return x[i][-1:] == x[0][0]
            elif (x[i][-1:] != x[i + 1][0]):
                return False
        return True
        
