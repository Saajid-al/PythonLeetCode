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
        s_, t_ = set(s), set(t)
        if s_!=t_:    
            return False
        for l in s_:
            if s.count(l)!= t.count(l):
                return False
        return True
        
s = Solution()
print(s.isAnagram("aacc","ccac"))