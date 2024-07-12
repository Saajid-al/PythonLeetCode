class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        x = 0
        for k,v  in enumerate(prices):
            if((max(prices[x:]) - (prices[k])) > maxProfit):
                maxProfit = max(prices[x:]) - (prices[k])
            x+=1
        return maxProfit


        #[2,0,5,1,10,9]
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))