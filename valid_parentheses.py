class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashmap = { ')':'(', '}':'{', ']':'['}

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped!= hashmap[c]:
                        return False
        return not stack





        #go through the list, if the first index has a clos
s = Solution()
print(s.isValid("()[]{}"))