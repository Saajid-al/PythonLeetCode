class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        print (n)
        #keep a previous holder
        previous = 0
        potentialSpot = 0
        for idx, i  in enumerate(flowerbed[:len(flowerbed)-1]):
            print("Previous Num : " , previous)
            nextElem = flowerbed[idx + 1]
            if i == 0 and nextElem == 0 and previous == 0:
                print("SUCCESS")
                potentialSpot = potentialSpot + 1
                previous = i
                if(potentialSpot) == n:
                    return True
            previous = i
            print("Current Index" , idx)
            print("Next Index", nextElem)
            print("____NEXT____")
        return False

                


             #[1 0 0 0 1]
             #[0 1 2 3 4]
                   
        
    #what we can do is just check how many spots are available
    #if index[i+1] and index [i-1] == 0
    #add that to our counter
    #then if it is less than or equal to our counter
    #we can return true or false
                

s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1], 1))