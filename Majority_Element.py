class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        oldCount = 0
        for x in nums:
            count = nums.count(x)
            if count > oldCount:
                count = oldCount
        return count
    
s = Solution()
s.majorityElement(3,[3,2,3])