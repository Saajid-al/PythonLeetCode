class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashset = {0 : 0}
        r = list(ransomNote)
        for idx, x in enumerate(magazine):
            hashset[idx] = x
            if(x in r):
                hashset.pop(idx)
                r.remove(x)

        if(not r):
            return True
        
        return False
s = Solution()
print(s.canConstruct("aa", "aab"))