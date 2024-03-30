class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        for c in chars:
            print(c)
        
s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))