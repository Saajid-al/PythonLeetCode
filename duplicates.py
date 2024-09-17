class Solution(object):
    def containsDuplicate(self, nums):

            nums.sort()
            n= len(nums)
            x = 0
            for i in range(1,n):
                if nums[i]==nums[i-1]:
                    x+= 1
                    if x > k:
                        return False
            return True

s = Solution()
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))