class Solution(object):
    def twoSum(self, nums, target):        

        newSet = {}


        for index, value in enumerate(nums) : 
            if(target-value in newSet):
                return([newSet[target-value],index])
            newSet[value] = index #we have the values as the keys because we want to find the values, and then return the index

        
s = Solution()
print(s.twoSum([2,7,11,15], 9))