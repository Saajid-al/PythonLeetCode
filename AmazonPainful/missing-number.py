from typing import Counter


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        N = len(nums)
        for i in range(N+1): #inclusive
            if i not in c:
                return i
        
s = Solution()
print(s.missingNumber([3,0,1])) 