class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #create a min array
        #create a max array
        #loop through !
        
        minI = 10**20
        minJ = 10**20
        #i=20 
        #20, 100, 10, 12, 5, 13
        for num in nums:
            if num <= minI:
                minI = num
            elif num <= minJ:
                minJ = num
            else:
                return True
        return False

s = Solution()    
print(s.increasingTriplet([20,100,10,12,5,13]))

#-3,4,6,7,8,-3,2
#for every element
#set i to be smallest
