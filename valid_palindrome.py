class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = 'a man,  a plan , a cala'
        p = p.join('a')
        print(p)
        s = ''.join(char.lower() for char in s if char.isalnum())
        return s == s[::-1]
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))