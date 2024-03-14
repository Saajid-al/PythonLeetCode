class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        
        """
        return str(x) == str(x)[::-1]
#TEST
s = Solution()
print(s.isPalindrome(121))

        
