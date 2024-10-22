class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l = 0 
        r = 0
        maxProfit = 0 
        while(r < len(prices)):
            if(prices[l] < prices[r] ) : 
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r 
            r+=1 
        return maxProfit
s = Solution()
print(s.maxProfit([7,1,5,3,6,4,0,9]))