class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #[3,2,1]
        #[0,1,2]
        list1 = [1]*len(nums)
        accumulator = 1
        accumulator2 = 1
        for i in range(len(nums)):
            list1[i] = accumulator
            accumulator = accumulator * nums[i]

        
        for i in range(len(nums)-1, -1, -1):
            list1[i] *= accumulator2
            accumulator2 *= nums[i]
        return list1



s = Solution()
print(s.productExceptSelf([1,2,3,4]))