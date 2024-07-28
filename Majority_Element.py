class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        num = 0
        for x in nums:
            if x == num:
                continue
            if nums.count(x) > count:
                count = nums.count(x)    
                num = x    
        return num
    
s = Solution()
print(s.majorityElement([3,2,3]))