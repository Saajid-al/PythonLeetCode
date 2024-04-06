class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        newNums = {}
        
        for idx, x in enumerate(nums):
            if abs(target-x) in newNums:
                return[newNums[target-x], idx]
            newNums[x] = idx




        
s = Solution()
print(s.twoSum([2,7,11,15], 9))