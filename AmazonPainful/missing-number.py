from typing import Counter


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        print(c)
s = Solution()
print(s.missingNumber([3,0,1])) 