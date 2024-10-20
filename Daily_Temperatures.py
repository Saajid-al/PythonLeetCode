class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0]*len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackIndex = stack.pop()[1]
                res[stackIndex] = i - stack[-1][1]
            stack.append([i,t])
        return res

s = Solution()
print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
            
             