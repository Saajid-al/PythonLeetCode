class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        res = 0
        while l<= r:
            m = l + ((r-l) //2)
            if m**2 > x: #check if the square of the number is greater than x
                r = m-1 #adjust binary search
            elif m**2 < x: #if it's not the biggest, it MIGHT be the number ,so we grab the largest number before it goes over x
                l = m+1 
                res = m #set rsult to m
            else:
                return m  #might actually be our result so we return mid
        return res
    
s = Solution()
print(s.mySqrt(4))