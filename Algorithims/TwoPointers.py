#Two pointers
#L and R
#get the sum of squares, and return it in reverse order - Sample question
#Squares of a Sorted Array

class Solution(object):
    def sortedSquares(self, nums):

        left = 0
        right = len(nums) - 1 
        results = []
        while left <= right:  #while left side is not equal to right side
            
            if abs(nums[left]) > abs(nums[right]): #checking if the abs value of the left is greater than the abs value of the right
                results.append(nums[left]**2) #squaring
                left += 1 #moving on
            else:
                results.append(nums[right]**2)
                right -= 1 
        return results[::-1]

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
