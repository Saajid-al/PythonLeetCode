class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min = nums[0]
        maxi = nums[0]

        for i in range(0,len(nums)-1, 1):
            for j in range(1, len(nums)-1, 1):
                if nums[i] < nums[j] < nums[j+1]:
                    return True
        return False

        # for i in range(0, len(nums)-1, 1):
        #     if(nums[i] < min):
        #         min = nums[i]
        #     if(nums[i]+1 > maxi):
        #         maxi = nums[i+1]
            
        #     if(min < nums[i] < maxi):
        #         return True
        # return False
        
s = Solution()    
print(s.increasingTriplet([1,2,3,4,5]))

#-3,4,6,7,8,-3,2
#for every element
#set i to be smallest
