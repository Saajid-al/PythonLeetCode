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

        for i in range(minimumWord):  #get the minimum length both words share
            str = str + word1[i]+word2[i] #add words
        if diff == 0: #if words were of equal length, return the string
            return str
        elif diff > 0: #if result is greater than 0, then print the rest of the resulting string
            return str+word1[len(word2):]    
        else:
                return str+word2[len(word1):] #if less than 0, again print the rest 


s = Solution()
print(s.mergeAlternately("ab","pqrs"))
