class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashmap = { ')':'(', '}':'{', ']':'['}

        for c in s:
            if c in hashmap:
                popped = stack.pop()
                if popped != hashmap[c]:
                    return False
            else:
                stack.append(c)
        if stack.isEmpty():
            return True
        else:
            return False




        #go through the list, if the first index has a clos
s = Solution()
print(s.isValid("()[]{}"))