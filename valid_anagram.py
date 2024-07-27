class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)):
            return False
        #aacc
        #ccc
        
        for x in t:
            if x not in s:
                return False
            s = s.replace(x,'',1)
            print(s)
        return True
        
s = Solution()
print(s.isAnagram("aacc","ccac"))