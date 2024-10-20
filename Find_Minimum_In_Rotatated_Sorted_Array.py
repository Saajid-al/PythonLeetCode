class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while  l <= r  :
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
             
            mid = (l+r) // 2 
            res = min(res, nums[mid])

       

            if(nums[mid] >= nums[l]):
                l = mid + 1 
            else:
                r = mid - 1 
        return res

s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
#3,4,5,1,2
#1,2
#1

# if mid > right, we are at a higher value. We need to move to the lower values
#if mid