class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        difference = len(word1)-len(word2)
        str = ""
        minWord = min(len(word1),len(word2))


        for i in range(minWord):
            str = str+word1[i] + word2[i]
        
        if difference == 0: 
            return str
        elif difference > 0:
            return str+word1[len(word2):]
        else:
            return str+word2[len(word1):]
        
        




s = Solution()
print(s.mergeAlternately("abc", "pqr"))