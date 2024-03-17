class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandy = max(candies)
        candyList = list()
        for i in range(len(candies)):
            if(candies[i] + extraCandies >= maxCandy):
                candyList.append(True)
            else:
                candyList.append(False)
        return candyList
            
            


        
s = Solution()
print(s.kidsWithCandies([2,3,5,1,3],3))