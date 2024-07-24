class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        print(s)
        for idx, x in enumerate(s):
            print(s[x])
s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")