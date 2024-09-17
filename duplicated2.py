class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums.sort()
        n = len(nums)

        x = 0

        for i,idx in enumerate(nums):
            for idx, j in enumerate(nums):
                if nums[i] == nums[j]:
                    x += 1
                    if (x >= k):
                        return True
                return False
            


s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))