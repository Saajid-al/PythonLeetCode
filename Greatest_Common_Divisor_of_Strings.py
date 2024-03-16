class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        #Can we pop the index from the string?
        #idea 2 : can we just mutiply the string by how many occurances exist ? 


        strlen = len(str1)
        strlen2 = len(str2)
        if str1+str2!=str2+str1: #if the string is not equal to each other when reversed, then they do not have any common divisor
            return ""
        elif str1 == str2: # if string is equal to each other we've reached
            return str1
        elif strlen > strlen2: 
            return self.gcdOfStrings(str1[strlen2:], str2)
        elif len(str2) > len(str1):
            return self.gcdOfStrings(str2[strlen:], str1)

s = Solution()
print(s.gcdOfStrings("ABABAB", "ABAB"))