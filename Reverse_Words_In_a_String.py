class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = s.strip().split()
        x = x[::-1]

        return ' '.join(x)
s = Solution()
print(s.reverseWords("the sky is blue"))