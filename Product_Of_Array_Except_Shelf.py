class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = 1
        zeroCounter = []
        for idx, x in enumerate(nums):
            if(x == 0):
                zeroCounter.append(idx)
                continue
            result = result * x

        if(len(zeroCounter) > 1):
            return [0] * len(nums)

        for idx, y in enumerate(nums):
            if 0 in nums:
                if nums[idx] == 0:
                    nums[idx] = result
                    continue
                elif nums[idx]!= 0:
                    nums[idx] = 0
                    continue
        nums[idx] = result//nums[idx]
        return nums
            
            
s = Solution()
print(s.productExceptSelf([-1,1,0,-3,0]))