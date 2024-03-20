class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        arr = []
        sList = list(s)
        for i in range(len(sList)):
            if sList[i] in vowels:
                arr.append(sList[i])

        for i in range(len(sList)):
            if sList[i] in vowels:
                sList[i] = arr.pop()
        s = ''.join(sList)
        return(s)

s = Solution()
print(s.reverseVowels("Hello"))

#record index ?
#reverse the string
#and put back into the index ? 