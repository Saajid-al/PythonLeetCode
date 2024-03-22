class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx, x in enumerate(nums):
            print(nums[idx])
            
s = Solution()
print(s.productExceptSelf([1,2,3,4]))