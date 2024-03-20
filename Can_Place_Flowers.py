class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        f = [0] + flowerbed + [0]
        for i in range(1, len(f) - 1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0: #create a new array to index from and just check
                f[i] = 1 #change the actual array
                n -= 1
        return n<=0
        
        
                


             #[1 0 0 0 1]
             #[0 1 2 3 4]
                   
        
    #what we can do is just check how many spots are available
    #if index[i+1] and index [i-1] == 0
    #add that to our counter
    #then if it is less than or equal to our counter
    #we can return true or false
                

s = Solution()
print(s.canPlaceFlowers([1,0,0,0,0,1], 2))