class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 1
        k=0
        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l
            

                

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))