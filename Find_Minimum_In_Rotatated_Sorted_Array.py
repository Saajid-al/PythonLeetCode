class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) -1

        res = nums[0]

        while(l <= r):
            
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if(nums[m] >= nums[r]):
                l = m+1
            else:
                r = m-1 
        return res
    
s = Solution()
print(s.findMin([3, 4, 5, 1, 2]))
