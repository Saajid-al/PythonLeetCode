class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l = 0
        r = 1
        maxProfit = 0
        while(r < len(prices)): #while our right pointer doesn't exceed the length of our prices 
            if prices[l] < prices[r]: #if the right pointer is greater
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r  #we found a new minimum
            r += 1 
        return maxProfit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
