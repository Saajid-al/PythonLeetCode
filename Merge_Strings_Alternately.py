class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        str = ""
        for index, x in enumerate(word1):
            if word1[index] is None:
                str = str+word2
            if word2[index] is None:
                str = str+word1
            str = str + word1[index]+word2[index]
        return str


s = Solution()
print(s.mergeAlternately("abc","pq"))
