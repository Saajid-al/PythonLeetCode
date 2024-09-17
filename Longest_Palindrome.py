class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        for x in s:
            p = s.count(x)
            print(p)   

s = Solution()
s.longestPalindrome("abccccdd")