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

















































        # min_price = float('inf')
        # max_profit = 0
        
        # for price in prices:
        #     if price < min_price:
        #         min_price = price
        #     elif price - min_price > max_profit:
        #         max_profit = price - min_price
        
        # return max_profit
    