class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        str = ""

        diff = len(word1) - len(word2) #get difference 
        minimumWord = min(len(word1),len(word2)) #minimum of both words

        for i in range(minimumWord):
            str = str + word1[i]+word2[i]
        if diff == 0:
            return str
        elif diff > 0:
            return str+word1[len(word2):]    
        else:
                return str+word2[len(word1):]


s = Solution()
print(s.mergeAlternately("ab","pqrs"))
