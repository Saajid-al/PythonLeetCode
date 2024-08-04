class Solution(object):
    def containsDuplicate(self, nums):

        return len(set(nums)) != len(nums)



s = Solution()
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))