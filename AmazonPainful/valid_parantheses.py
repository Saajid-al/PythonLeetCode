class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype
        """

        stack = []

        map = { ')':'(', ']':'[','}':'{' }

        for i in s:
            if i in map:
                if stack and stack[-1] == map[i]:
                    stack.pop
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

        #([])