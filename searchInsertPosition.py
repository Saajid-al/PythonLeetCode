class Solution(object):
    def searchInsert(self, nums, target):

        l = 0
        r = len(nums)-1

        while(l < r):
            mid = (l+r)//2

            if(nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                l = mid+l
            else:
                r = mid -1 

        if mid > target:
            return mid + 1
        elif mid < target:
            return mid - 1
        

             

s = Solution()
print(s.searchInsert([1,3,5,6], 7))