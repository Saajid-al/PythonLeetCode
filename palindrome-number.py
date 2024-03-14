class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        
        """
        y = str(x)
        x = str(x)
        y = y[::-1]
        print(x)
        print(y)
        if y == x:
            return True
        else:
            return False
        
