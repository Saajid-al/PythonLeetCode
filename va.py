class Solution(object):
    def binarySearch(self, nums, target):

        l = 0
        r = len(nums)-1

        while l < r :
            middle = (l + r) // 2
            if nums[middle]== target:
                return middle
            elif nums[middle] > target:
                middle = l+1
            else : 
                middle = r-1
            return middle

s = Solution()
print(s.binarySearch([1,2,3,4,6,9,10,23,29], 23))
        
        