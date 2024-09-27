#Two pointers
#L and R
#get the sum of squares, and return it in reverse order - Sample question
#Squares of a Sorted Array

class Solution(object):
    def sortedSquares(self, nums):

        left = 0
        right = len(nums) - 1 
        results = []
        while left <= right: 
            
            if abs(nums[left]) > abs(nums[right]):
                results.append(nums[left]**2)
                left += 1
            else:
                results.append(nums[right]**2)
                right += 1 
        return results

s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
